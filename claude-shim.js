/*
 * claude-shim.js — "modo local" da Central de Conteúdo SCI-AGRO.
 *
 * A Central foi feita para rodar dentro do claude.ai, onde o próprio Claude
 * fornece o banco de dados compartilhado (window.claude: db, user, assets,
 * downloads). Fora do claude.ai (GitHub Pages, servidor próprio, arquivo
 * aberto no navegador) esse objeto não existe.
 *
 * Este arquivo cria uma versão simples desse objeto, guardando tudo no
 * localStorage do navegador e começando pelos dados de data/posts.json e
 * data/ideias.json. Limites do modo local:
 *   - os dados ficam só neste navegador (não são compartilhados com a gestora);
 *   - não há upload de artes (use links do Google Drive no post);
 *   - o nome de quem aprova vem do campo "Seu nome" no topo da página.
 *
 * Dentro do claude.ai este arquivo não faz nada.
 */
(function () {
  if (window.claude && window.claude.use) return;

  var KEY = 'sci-central-db-v1';
  var ME = 'local';
  var store = null;
  var listeners = [];
  var ready = null;

  function load() {
    try { var raw = localStorage.getItem(KEY); if (raw) return JSON.parse(raw); } catch (_) {}
    return null;
  }
  function persist() {
    try { localStorage.setItem(KEY, JSON.stringify(store)); } catch (_) {}
  }
  function seed() {
    var get = function (f) {
      return fetch(f, { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : {}; }).catch(function () { return {}; });
    };
    return Promise.all([get('data/posts.json'), get('data/ideias.json')]).then(function (r) {
      return { posts: r[0] || {}, ideias: r[1] || {} };
    });
  }
  function init() {
    if (!ready) {
      ready = Promise.resolve(load()).then(function (s) {
        if (s) { store = s; return; }
        return seed().then(function (s2) { store = s2; persist(); });
      });
    }
    return ready;
  }

  function coll(name) { if (!store[name]) store[name] = {}; return store[name]; }
  function snapshot(name, field, dir) {
    var c = coll(name);
    var docs = Object.keys(c).map(function (id) {
      var d = c[id];
      return { id: id, data: function () { return JSON.parse(JSON.stringify(d)); } };
    });
    if (field) {
      docs.sort(function (a, b) {
        var x = c[a.id][field], y = c[b.id][field];
        var r = x < y ? -1 : x > y ? 1 : 0;
        return dir === 'desc' ? -r : r;
      });
    }
    return { docs: docs, size: docs.length, empty: !docs.length };
  }
  function notify(name) {
    persist();
    listeners.forEach(function (l) {
      if (l.name === name) { try { l.cb(snapshot(name, l.field, l.dir)); } catch (e) { console.error(e); } }
    });
  }
  function query(name, field, dir) {
    return {
      orderBy: function (f, d) { return query(name, f, d); },
      onSnapshot: function (cb, err) {
        var l = { name: name, field: field, dir: dir, cb: cb };
        listeners.push(l);
        setTimeout(function () { cb(snapshot(name, field, dir)); }, 0);
        return function () { listeners = listeners.filter(function (x) { return x !== l; }); };
      },
      get: function () { return Promise.resolve(snapshot(name, field, dir)); }
    };
  }
  var db = {
    collection: function (name) {
      var q = query(name);
      q.add = function (data) {
        var id = 'loc-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
        coll(name)[id] = JSON.parse(JSON.stringify(data));
        notify(name);
        return Promise.resolve({ id: id });
      };
      q.doc = function (id) { return db.doc(name + '/' + id); };
      return q;
    },
    doc: function (path) {
      var p = path.split('/'), name = p[0], id = p[1];
      return {
        id: id,
        get: function () { var d = coll(name)[id]; return Promise.resolve({ id: id, exists: !!d, data: function () { return d ? JSON.parse(JSON.stringify(d)) : undefined; } }); },
        set: function (data) { coll(name)[id] = JSON.parse(JSON.stringify(data)); notify(name); return Promise.resolve(); },
        update: function (patch) {
          var c = coll(name);
          if (!c[id]) return Promise.reject({ code: 'not_found', message: 'Documento não encontrado' });
          Object.keys(patch).forEach(function (k) { c[id][k] = JSON.parse(JSON.stringify(patch[k])); });
          notify(name);
          return Promise.resolve();
        },
        delete: function () { delete coll(name)[id]; notify(name); return Promise.resolve(); }
      };
    }
  };

  function nome() { try { return localStorage.getItem('sci-central-nome') || ''; } catch (_) { return ''; } }
  function avatar(txt) {
    var ini = (txt || '?').trim().split(/\s+/).map(function (w) { return w[0]; }).join('').slice(0, 2).toUpperCase() || '?';
    var svg = '<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56"><rect width="56" height="56" rx="28" fill="#0054A6"/>' +
      '<text x="28" y="35" font-family="Arial" font-size="22" font-weight="700" fill="#fff" text-anchor="middle">' + ini + '</text></svg>';
    return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
  }
  var user = {
    me: function () { var n = nome(); return Promise.resolve({ id: ME, name: n, avatarUrl: avatar(n), color: '#0054A6', email: null, isOwner: true, canEdit: true }); },
    id: function () { return Promise.resolve(ME); },
    name: function () { return Promise.resolve(nome()); },
    isOwner: function () { return Promise.resolve(true); },
    canEdit: function () { return Promise.resolve(true); },
    can: function () { return Promise.resolve(true); },
    profiles: function (ids) {
      var out = {};
      [].concat(ids || []).forEach(function (id) {
        var mine = id === ME;
        out[id] = { id: id, name: mine ? nome() : '', avatarUrl: avatar(mine ? nome() : ''), color: '#7A93A6', email: null, isMe: mine, guest: false };
      });
      return Promise.resolve(out);
    },
    search: function () { return Promise.resolve([]); }
  };
  var downloads = {
    save: function (o) {
      var a = document.createElement('a');
      a.href = URL.createObjectURL(o.data);
      a.download = o.filename || 'arquivo';
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
      return Promise.resolve();
    }
  };

  window.claude = {
    local: true,
    use: function (name) {
      if (name === 'db') return init().then(function () { return db; });
      if (name === 'user') return Promise.resolve(user);
      if (name === 'downloads') return Promise.resolve(downloads);
      return Promise.resolve(null); // assets: sem upload no modo local
    }
  };

  /* ---------- faixa "modo local": backup, importar, restaurar ---------- */
  function bar() {
    var b = document.createElement('div');
    b.id = 'local-bar';
    b.setAttribute('role', 'region');
    b.setAttribute('aria-label', 'Modo local');
    b.style.cssText = 'position:fixed;left:0;right:0;bottom:0;z-index:40;display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center;justify-content:center;' +
      'padding:8px 16px calc(8px + env(safe-area-inset-bottom,0px));background:#FFF6E0;border-top:1px solid #E0A21B;color:#6B4700;font:13px/1.4 Figtree,system-ui,sans-serif';
    b.innerHTML = '<span><b>Modo local:</b> os dados ficam só neste navegador. Artes: use links do Google Drive.</span>' +
      '<button type="button" data-lb="exp">Baixar backup (JSON)</button>' +
      '<label style="cursor:pointer;text-decoration:underline">Importar backup<input type="file" accept="application/json" data-lb="imp" hidden></label>' +
      '<button type="button" data-lb="reset">Voltar aos dados do repositório</button>';
    Array.prototype.forEach.call(b.querySelectorAll('button'), function (x) {
      x.style.cssText = 'border:1px solid #E0A21B;background:#fff;color:#6B4700;border-radius:6px;padding:4px 10px;font:inherit;font-weight:600;cursor:pointer';
    });
    document.body.appendChild(b);
    document.body.style.paddingBottom = '56px';
    b.addEventListener('click', function (e) {
      var t = e.target.closest('[data-lb]'); if (!t) return;
      if (t.dataset.lb === 'exp') {
        init().then(function () {
          var blob = new Blob([JSON.stringify(store, null, 1)], { type: 'application/json' });
          downloads.save({ filename: 'central-sci-agro-backup-' + new Date().toISOString().slice(0, 10) + '.json', data: blob });
        });
      }
      if (t.dataset.lb === 'reset') {
        if (!confirm('Apagar as mudanças feitas neste navegador e voltar aos dados do repositório?')) return;
        try { localStorage.removeItem(KEY); } catch (_) {}
        location.reload();
      }
    });
    b.addEventListener('change', function (e) {
      var inp = e.target; if (inp.dataset.lb !== 'imp' || !inp.files[0]) return;
      inp.files[0].text().then(function (txt) {
        var s = JSON.parse(txt);
        if (!s || typeof s.posts !== 'object') throw new Error('arquivo inválido');
        store = { posts: s.posts, ideias: s.ideias || {} };
        persist(); notify('posts'); notify('ideias');
        alert('Backup importado.');
      }).catch(function () { alert('Não foi possível ler esse arquivo. Use um backup baixado por esta página.'); });
      inp.value = '';
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', bar); else bar();
})();
