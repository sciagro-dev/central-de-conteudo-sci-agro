"""Gera ../index.html a partir do molde central.html.

Uso (na pasta src/):  python3 build.py

- Preenche os textos fixos da página (quadros, rota da Área do Mês, insights,
  stories extras e link do documento do time), que vêm de quadros.py e data_q4.py.
- Monta um documento HTML completo (o claude.ai acrescenta <html>/<head>
  sozinho; fora dele a página precisa disso).
- Coloca o claude-shim.js antes do script principal: fora do claude.ai ele
  cria o "modo local"; dentro do claude.ai não faz nada.

Os POSTS e as IDEIAS não entram no HTML: ficam em ../data/*.json (modo local)
ou no banco do artefato no claude.ai.
"""
import json
import os

from data_q4 import DOC, AREAS, INSIGHTS, EXTRAS
from quadros import QUADROS

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)

h = open(os.path.join(AQUI, "central.html"), encoding="utf-8").read()
h = (h.replace("__QUADROS__", json.dumps(QUADROS, ensure_ascii=False))
      .replace("__DOC__", DOC)
      .replace("__AREAS__", json.dumps(AREAS, ensure_ascii=False))
      .replace("__INSIGHTS__", json.dumps(INSIGHTS, ensure_ascii=False))
      .replace("__EXTRAS__", json.dumps([[a, b] for a, b, c in EXTRAS], ensure_ascii=False)))

# versão para o claude.ai (conteúdo do artefato, sem <html>/<head>)
open(os.path.join(RAIZ, "artifact.html"), "w", encoding="utf-8").write(h)

# versão autônoma (GitHub Pages / servidor / navegador)
corte = h.index("<header")
cabeca, corpo = h[:corte], h[corte:]
i = corpo.index("<script>")
corpo = corpo[:i] + '<script src="claude-shim.js"></script>\n' + corpo[i:]
pagina = (
    "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
    "<meta name=\"robots\" content=\"noindex,nofollow\">\n"
    + cabeca.strip() + "\n</head>\n<body>\n" + corpo.strip() + "\n</body>\n</html>\n"
)
open(os.path.join(RAIZ, "index.html"), "w", encoding="utf-8").write(pagina)
print("ok:", os.path.join(RAIZ, "index.html"), len(pagina), "bytes")
