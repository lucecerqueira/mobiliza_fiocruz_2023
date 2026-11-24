import random
import re

ABERTURAS = [
    "Ministra @belchiormiriam, a Fiocruz é essencial para o SUS",
    "Fortalecer o SUS começa por valorizar quem faz ciência! Ministra @belchiormiriam",
    "Ministra @belchiormiriam, a saúde pública brasileira precisa da Fiocruz operando com força máxima",
    "O Brasil precisa de mais ciência e mais servidores no SUS! Ministra @belchiormiriam",
    "Ministra @belchiormiriam, cada pesquisa e vacina da Fiocruz salva vidas em todo o país",
    "Em defesa da ciência e da saúde pública: Ministra @belchiormiriam",
    "Ministra @belchiormiriam, a Fiocruz é patrimônio estratégico do Brasil e pilar do SUS",
    "Sem servidores não há pesquisa nem produção de vacinas! Ministra @belchiormiriam",
    "Ministra @belchiormiriam, investir na Fiocruz é garantir soberania sanitária para o Brasil",
    "Atenção, Ministra @belchiormiriam! A Fiocruz precisa recompor urgentemente seu quadro de servidores",
    "Ministra @belchiormiriam, o SUS depende da excelência científica da Fiocruz",
    "Mais ciência, mais saúde, mais SUS! Ministra @belchiormiriam",
]

NUCLEOS = [
    "e suas pesquisas impactam diretamente a vida de milhões de pessoas.",
    "e o déficit de pessoal ameaça entregas estratégicas para a população.",
    "e centenas de aprovados no último concurso estão prontos para assumir imediatamente.",
    "com profissionais altamente qualificados aguardando apenas a autorização de nomeação.",
    "para ampliar a vigilância em saúde, a produção de vacinas e o atendimento no SUS.",
    "e a recomposição da força de trabalho é urgente para manter a excelência institucional.",
    "com especialistas aprovados em concurso público prontos para somar à saúde brasileira.",
    "e cada dia de espera atrasa pesquisas vitais para a população brasileira.",
    "para fortalecer nossas unidades de pesquisa e produção em todo o território nacional.",
    "e os excedentes aprovados representam reforço imediato e qualificado para o país.",
]

CHAMADAS = [
    "Convoque os excedentes do último concurso: são centenas de profissionais qualificados prontos para somar ao SUS!",
    "Autorize a convocação dos excedentes do concurso Fiocruz 2023 agora!",
    "Libere a nomeação dos aprovados excedentes e fortaleça o SUS!",
    "Convoque os excedentes aprovados! O Brasil precisa desses profissionais atuando na saúde pública.",
    "Dê o próximo passo pelo fortalecimento do SUS e autorize a chamada dos excedentes da Fiocruz!",
    "Nomeie os excedentes do último certame: a saúde pública brasileira agradece!",
    "Autorize a convocação imediata dos excedentes aprovados no concurso da Fiocruz!",
    "Convoque os aprovados excedentes e garanta mais força de trabalho para a ciência nacional!",
    "O SUS precisa desses especialistas! Autorize a convocação dos excedentes da Fiocruz.",
    "Chamada dos excedentes já! Profissionais prontos para servir ao SUS e à ciência.",
]

MOLDURAS_EMOJI = [
    ("🇧🇷‼️🇧🇷🇧🇷🇧🇷🇧🇷‼️🇧🇷🇧🇷🇧🇷‼️🇧🇷‼️", "🇧🇷‼️🇧🇷🇧🇷🇧🇷🇧🇷‼️🇧🇷🇧🇷🇧🇷‼️🇧🇷‼️"),
    ("🚨🇧🇷🚨🇧🇷🚨🇧🇷🚨🇧🇷🚨", "🚨🇧🇷🚨🇧🇷🚨🇧🇷🚨🇧🇷🚨"),
    ("🇧🇷📢🇧🇷📢🇧🇷📢🇧🇷", "🇧🇷📢🇧🇷📢🇧🇷📢🇧🇷"),
    ("‼️🇧🇷‼️🇧🇷‼️🇧🇷‼️", "‼️🇧🇷‼️🇧🇷‼️🇧🇷‼️"),
    ("🇧🇷🔬🇧🇷💉🇧🇷🏥🇧🇷", "🇧🇷🔬🇧🇷💉🇧🇷🏥🇧🇷"),
    ("⚡🇧🇷⚡🇧🇷⚡🇧🇷⚡", "⚡🇧🇷⚡🇧🇷⚡🇧🇷⚡"),
]


def _extrair_arrobas_e_hashtags(texto_base):
    arrobas = re.findall(r"@\w+", texto_base)
    hashtags = re.findall(r"#\w+", texto_base)
    arroba_principal = arrobas[0] if arrobas else "@belchiormiriam"
    hashtag_principal = " ".join(dict.fromkeys(hashtags)) if hashtags else "#ConvocaFiocruz"
    return arroba_principal, hashtag_principal


def gerar_lote_impulsionamento(texto_base, quantidade=50, arroba_custom="", hashtag_custom=""):
    """
    Gera até 200 variações únicas combinando estrutura, argumentos, menções e molduras
    para evitar bloqueio por repetição idêntica nas redes sociais.
    """
    quantidade = max(1, min(int(quantidade), 200))
    arroba_detectada, hashtag_detectada = _extrair_arrobas_e_hashtags(texto_base)
    arroba = arroba_custom.strip() or arroba_detectada
    if arroba and not arroba.startswith("@"):
        arroba = f"@{arroba}"

    hashtag = hashtag_custom.strip() or hashtag_detectada
    if hashtag and not hashtag.startswith("#"):
        hashtag = f"#{hashtag}"

    combinacoes = []
    # Garante o texto original como primeira opção
    texto_limpo = texto_base.strip()
    if texto_limpo:
        combinacoes.append(texto_limpo)

    # Gera pool combinatório único
    pool = []
    for ab in ABERTURAS:
        for nuc in NUCLEOS:
            for ch in CHAMADAS:
                ab_ajustada = ab.replace("@belchiormiriam", arroba)
                corpo = f"{ab_ajustada}, {nuc} {ch} {hashtag}"
                pool.append(corpo)

    random.shuffle(pool)

    for idx, corpo in enumerate(pool):
        if len(combinacoes) >= quantidade:
            break
        topo, base = MOLDURAS_EMOJI[idx % len(MOLDURAS_EMOJI)]
        msg_final = f"{topo}\n{corpo}\n{base}"
        if msg_final not in combinacoes:
            combinacoes.append(msg_final)

    return combinacoes