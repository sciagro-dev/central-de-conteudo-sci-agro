# Central de Conteúdo SCI-AGRO

Sistema de planejamento e aprovação dos posts do Instagram (@sciagrolab) e do LinkedIn da SCI-AGRO, de outubro a dezembro de 2026. Reúne o cronograma, o fluxo de aprovação em duas etapas (revisão técnica da área e aprovação final da gestora), os quadros de conteúdo, as pautas sugeridas pelas áreas e o radar semanal.

> **Conteúdo interno.** Os dados trazem posts ainda não aprovados, briefings, benefícios e regras de sigilo BPL. Mantenha este repositório **privado** (veja "Publicar" abaixo).

## Onde a Central roda

| Onde | Como os dados ficam | Para quê |
|---|---|---|
| **claude.ai** (versão oficial) | Banco compartilhado do próprio claude.ai: todo mundo que abre o link vê e aprova a mesma coisa | Uso do dia a dia com a gestora e as áreas |
| **Modo local** (este repositório) | No navegador de quem abre (`localStorage`), começando pelos dados de `data/` | Cópia de segurança, versionamento, rodar fora do Claude |

No modo local, uma faixa amarela no rodapé lembra que os dados não são compartilhados e oferece **Baixar backup**, **Importar backup** e **Voltar aos dados do repositório**. Não há upload de artes no modo local: use o campo de link (Google Drive) dentro do post.

## Estrutura

```
index.html          página pronta para abrir fora do claude.ai (gerada pelo build)
artifact.html       a mesma página no formato do artefato do claude.ai (gerada pelo build)
claude-shim.js      cria o "modo local" quando a página não está no claude.ai
data/posts.json     posts (id = data AAAA-MM-DD), com etapas, legendas, briefing e histórico
data/ideias.json    pautas das áreas e ideias do radar semanal
src/central.html    molde da página (HTML, CSS e JavaScript)
src/quadros.py      definição dos 8 quadros de conteúdo
src/data_q4.py      rota da Área do Mês, insights, stories extras (e dados usados na primeira carga)
src/data.py, src/data_v1.py   dados de origem do cronograma de outubro
src/build.py        gera index.html e artifact.html
```

Dados exportados da Central em 29/09/2026 (27 posts e 9 ideias).

## Rodar no computador

A página precisa ser servida por HTTP (abrir o arquivo com dois cliques não carrega `data/`):

```bash
cd central-conteudo-sci-agro
python3 -m http.server 8000
# abra http://localhost:8000
```

## Alterar a página

1. Edite `src/central.html` (visual e comportamento) ou `src/quadros.py` / `src/data_q4.py` (textos fixos).
2. Rode `python3 src/build.py`. Ele gera `index.html` e `artifact.html`.
3. Para atualizar a versão oficial no claude.ai, peça ao Claude para republicar `artifact.html` no mesmo link da Central (os dados do banco não mudam).

## Atualizar os dados do repositório

Os dados vivos estão no claude.ai. Para trazer uma cópia nova, peça ao Claude: *"exporte os posts e as ideias da Central para data/posts.json e data/ideias.json"*. Faça isso no fim de cada mês, junto com o CSV (botão "Exportar planilha").

## Publicar

- **Repositório privado:** recomendado. Crie o repositório como *Private* no GitHub.
- **GitHub Pages:** funciona (a página é estática), mas **um site do GitHub Pages fica público na internet mesmo quando o repositório é privado**, e Pages em repositório privado exige plano pago. Como os dados são internos, não publique pelo Pages. Para a equipe, use o link do claude.ai.

## Subir para o GitHub

```bash
cd central-conteudo-sci-agro
git init
git add .
git commit -m "Central de Conteúdo SCI-AGRO"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/central-conteudo-sci-agro.git
git push -u origin main
```

Ou, sem terminal: no GitHub, **New repository → Private → uploading an existing file**, e arraste o conteúdo desta pasta.

## Regras de conteúdo (resumo)

- Sigilo BPL: nada de etiqueta, código de estudo, tela legível, nome de patrocinador; nenhuma imagem de animal.
- Filmar área de teste só com liberação da Garantia da Qualidade.
- Prazos automáticos: arte até 7 dias antes, revisão técnica até 5, aprovação final até 3.
