from data_v1 import POSTS as V1, EXTRAS as X1
DOC = "https://docs.google.com/document/d/1KewyEvOG5zNlui9IXQ8eEuO3y3SewxwhxlTjueU8q0A/edit"
old = {p["n"]: p for p in V1}

def keep(n, **kw):
    p = dict(old[n]); p.update(kw); p.setdefault("status", "Novo"); return p

A1 = {"data":"06/10","dia":"Ter","hora":"12h","formato":"Arte estática","tipo":"Arte","pilar":"Institucional",
 "tema":"Seu produto. Nossa responsabilidade.","status":"Aprovado",
 "objetivo":"Reforçar o posicionamento da SCI-AGRO como parceira técnica. Abre o mês e apresenta a marca para quem chega.",
 "laminas":["Arte clean, fundo claro, azul e verde. Texto: 'Testes e estudos com responsabilidade para apoiar decisões'. CTA: 'Fale com nossa equipe'. (Direção do documento aprovado: conferir lá antes de produzir.)"],
 "legenda":"USAR A LEGENDA APROVADA: Post 1 do documento de cronograma (abre com \"Seu produto. Nossa responsabilidade.\"). Não reescrever.",
 "legenda_li":"Mesma legenda aprovada (Post 1). No LinkedIn, manter o texto e usar só 3 a 5 hashtags.",
 "roteiro":"","fonte":"Documento de cronograma (Arte 1 e Post 1), aprovado.","atencao":"Copiar a legenda direto do documento, sem redigitar."}
A3 = {"data":"08/10","dia":"Qui","hora":"12h","formato":"Arte estática","tipo":"Arte","pilar":"Saneantes",
 "tema":"Comprovar eficácia é essencial para inseticida","status":"Aprovado",
 "objetivo":"Apresentar os estudos de eficácia para inseticidas domissanitários a fabricantes de household.",
 "laminas":["Linguagem household, ícones de mosquito, mosca, barata e formiga, fundo branco com azul e verde. CTA: 'Solicite informações sobre estudos de eficácia'. (Direção do documento aprovado: conferir lá antes de produzir.)"],
 "legenda":"USAR A LEGENDA APROVADA: Post 3 do documento de cronograma (inseticidas: mosquitos, moscas, baratas e formigas). Não reescrever.",
 "legenda_li":"Mesma legenda aprovada (Post 3). No LinkedIn, trocar os emojis de insetos por uma linha simples e usar 3 a 5 hashtags.",
 "roteiro":"","fonte":"Documento de cronograma (Arte 3 e Post 3), aprovado.","atencao":"Copiar a legenda direto do documento, sem redigitar."}
A4 = {"data":"22/10","dia":"Qui","hora":"12h","formato":"Arte estática","tipo":"Arte","pilar":"Saneantes",
 "tema":"Desinfetante eficaz precisa de comprovação","status":"Aprovado",
 "objetivo":"Apresentar os ensaios microbiológicos de eficácia de desinfetantes.",
 "laminas":["Visual técnico e moderno, ícones de microrganismo, superfície e laudo. Listar: bactericida, fungicida, micobactericida, esporicida/esterilizante. CTA: 'Converse com nossa equipe técnica'. (Direção do documento aprovado: conferir lá antes de produzir.)"],
 "legenda":"USAR A LEGENDA APROVADA: Post 4 do documento de cronograma (abre com \"Desinfetante eficaz precisa de comprovação.\"). Não reescrever.",
 "legenda_li":"Mesma legenda aprovada (Post 4). No LinkedIn, manter a lista com ✔️ e usar 3 a 5 hashtags.",
 "roteiro":"","fonte":"Documento de cronograma (Arte 4 e Post 4), aprovado.","atencao":"Copiar a legenda direto do documento, sem redigitar. O checklist do documento pede validar os termos esporicida/esterilizante e micobactericida com o time técnico."}

LI = {
 3: "Hoje, 12 de outubro, é Dia do Engenheiro Agrônomo.\n\nNa SCI-AGRO, agrônomos ajudam a ligar o que acontece na lavoura ao que é avaliado no laboratório: do desenho de estudos à interpretação de dados que sustentam o registro de novos produtos.\n\nNosso agradecimento aos profissionais do time que fazem essa ponte todos os dias.\n\n#SCIAGRO #DiaDoEngenheiroAgrônomo #Agronomia #Agronegócio",
 4: "Estudos de ecotoxicologia com abelhas exigem cuidado antes mesmo do ensaio começar.\n\nNa SCI-AGRO, avaliamos efeitos de produtos sobre abelhas e larvas, por via oral e por contato, em testes agudos e crônicos. O condicionamento das espécies segue cada guia de teste, e as condições climáticas são controladas durante todo o estudo.\n\nÉ esse controle que dá sustentação técnica ao resultado entregue ao patrocinador.\n\nNo vídeo, um pouco da rotina do nosso laboratório de Ecotoxicologia.\n\n#SCIAGRO #Ecotoxicologia #Polinizadores #BPL #EstudosRegulatórios",
 5: "16 de outubro, Dia Mundial da Alimentação.\n\nUma etapa pouco visível da segurança alimentar acontece no laboratório: o estudo de resíduos de defensivos agrícolas, que mede o que permanece no alimento após a aplicação e apoia a definição de limites seguros de uso.\n\nNa SCI-AGRO, conduzimos a fase analítica desses estudos:\n• desenvolvimento e validação de métodos\n• cromatografia líquida (LC/MSMS) e gasosa (CG/MS)\n• possibilidade de atuação como Pesquisador Principal ou Diretor de Estudo\n\n#SCIAGRO #SegurançaAlimentar #ResíduosDePesticidas #Cromatografia #Agronegócio",
 6: "O mercado de bioinsumos cresce rápido, e a exigência por dados sólidos cresce junto.\n\nPara um biopesticida chegar ao mercado, algumas perguntas precisam de resposta de laboratório:\n• É o microrganismo declarado? Identificação por qPCR.\n• Está na concentração declarada e livre de contaminantes e toxinas relevantes?\n• Continua estável até o fim da validade?\n• É seguro? Testes de toxicidade e patogenicidade.\n\nA SCI-AGRO apoia empresas de biológicos e fitoquímicos em cada uma dessas etapas. Fale com o nosso time: sales@sci-agro.com\n\n#SCIAGRO #Bioinsumos #Biopesticidas #Microbiologia #ControleBiológico",
 8: "Um bioinsumo é um produto vivo. Como o laboratório garante que ele é o que diz ser e que continua funcionando até o fim da validade?\n\nNeste vídeo, nosso time de Microbiologia explica as quatro perguntas que todo biológico precisa responder: identidade, concentração, pureza e estabilidade.\n\nFicou alguma dúvida? Deixe nos comentários.\n\n#SCIAGRO #Bioinsumos #Microbiologia #Biopesticidas #EstudosRegulatórios",
}
def k(n, **kw): return keep(n, legenda_li=LI[n], **kw)

POSTS = [A1, A3,
 k(3), k(4), k(5), k(6),
 A4,
 k(8)]
for i,p in enumerate(POSTS,1): p["n"]=i
# ajustar atenção do vídeo de bioinsumo (tema sai do carrossel de 20/10)
POSTS[5]["atencao"] = old[6]["atencao"]

PROXIMO = [
 ("Novo", "Carrossel", "Saneantes", "Seu saneante é risco 1 ou risco 2?", "Pronto no cronograma anterior. Casa bem com o post de desinfetantes (desinfetante é risco 2 por ter ação antimicrobiana)."),
 ("Novo", "Carrossel", "Ciência sem jargão", "In vivo, in vitro, in silico: qual a diferença?", "Pronto no cronograma anterior."),
 ("Documento", "Carrossel", "Autoridade técnica", "O que torna uma análise confiável?", "Legenda já escrita no documento (Post 2), falta aprovação."),
 ("Documento", "Vídeo", "Bastidores", "Por dentro da SCI-AGRO", "Ideia do documento (Vídeo 1)."),
 ("Documento", "Vídeo", "Saneantes", "Como funciona um estudo de eficácia?", "Ideia do documento (Vídeo 2). Bom par para os posts de inseticida e desinfetante."),
 ("Documento", "Carrossel", "Household", "Produtos household: segurança também precisa de ciência", "Ideia do documento (Arte 5)."),
 ("Documento", "Arte", "Pessoas", "Ciência feita por pessoas", "Ideia do documento (Arte 6)."),
]
EXTRAS = X1
