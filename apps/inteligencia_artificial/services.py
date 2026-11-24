import random
import re


class MotorImpulsionamento:
    ABERTURAS_COM_DESTINATARIO = [
        "{destinatario}, a Fiocruz é essencial para o SUS.",
        "Fortalecer o SUS começa por valorizar a ciência! {destinatario}, a Fiocruz é pilar da saúde pública.",
        "{destinatario}, a saúde pública brasileira precisa da Fiocruz operando com força máxima.",
        "O Brasil precisa de mais ciência e mais servidores! {destinatario}, a Fiocruz é estratégica para o país.",
        "{destinatario}, cada pesquisa e vacina da Fiocruz salva vidas em todo o Brasil.",
        "Em defesa da ciência e da saúde pública: {destinatario}, a Fiocruz sustenta políticas vitais do SUS.",
        "{destinatario}, a Fiocruz é patrimônio estratégico do Brasil e referência no SUS.",
        "Sem servidores não há pesquisa nem produção de vacinas! {destinatario}, a Fiocruz precisa de reforço.",
        "{destinatario}, investir na Fiocruz é garantir soberania sanitária para o Brasil.",
        "Atenção, {destinatario}: a Fiocruz precisa recompor urgentemente seu quadro de servidores.",
        "{destinatario}, o SUS depende da excelência científica e tecnológica da Fiocruz.",
        "Mais ciência, mais saúde, mais SUS! {destinatario}, a Fiocruz faz a diferença na vida da população.",
    ]

    ABERTURAS_NEUTRAS = [
        "A Fiocruz é essencial para o SUS.",
        "Fortalecer o SUS começa por valorizar quem faz ciência na Fiocruz.",
        "A saúde pública brasileira precisa da Fiocruz operando com força máxima.",
        "O Brasil precisa de mais ciência e mais servidores na Fiocruz.",
        "Cada pesquisa e vacina da Fiocruz salva vidas em todo o país.",
        "A Fiocruz é patrimônio estratégico do Brasil e pilar do SUS.",
        "Sem servidores não há pesquisa nem produção de vacinas na Fiocruz.",
        "Investir na Fiocruz é garantir soberania sanitária para o Brasil.",
        "A Fiocruz precisa recompor urgentemente seu quadro de servidores.",
        "O SUS depende da excelência científica e tecnológica da Fiocruz.",
    ]

    NUCLEOS = [
        "Suas pesquisas impactam diretamente a vida de milhões de pessoas.",
        "O déficit de pessoal ameaça entregas estratégicas para a população.",
        "Centenas de aprovados no último concurso estão prontos para assumir imediatamente.",
        "São profissionais altamente qualificados aguardando apenas a autorização de nomeação.",
        "Esse reforço amplia a vigilância em saúde, a produção de vacinas e o atendimento no SUS.",
        "A recomposição da força de trabalho é urgente para manter a excelência institucional.",
        "Há especialistas aprovados em concurso público prontos para somar à saúde brasileira.",
        "Cada dia de espera atrasa pesquisas vitais para a população brasileira.",
        "É fundamental fortalecer nossas unidades de pesquisa e produção em todo o território nacional.",
        "Os excedentes aprovados representam reforço imediato e qualificado para o país.",
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

    def __init__(self, texto_base, arroba_custom="", hashtag_custom="", tratamento=""):
        self.texto_base = (texto_base or "").strip()
        self.arroba = self._resolver_arroba(arroba_custom)
        self.hashtag = self._resolver_hashtag(hashtag_custom)
        self.tratamento = (tratamento or "").strip()
        self.destinatario = self._montar_destinatario()

    def _resolver_arroba(self, arroba_custom):
        valor = (arroba_custom or "").strip()
        if not valor:
            encontrados = re.findall(r"@[\w.]+", self.texto_base)
            valor = encontrados[0] if encontrados else ""
        if valor and not valor.startswith("@"):
            valor = f"@{valor}"
        return valor

    def _resolver_hashtag(self, hashtag_custom):
        valor = (hashtag_custom or "").strip()
        if not valor:
            encontradas = re.findall(r"#\w+", self.texto_base)
            valor = " ".join(dict.fromkeys(encontradas)) if encontradas else "#ConvocaFiocruz"
        elif not valor.startswith("#"):
            valor = f"#{valor}"
        return valor

    def _montar_destinatario(self):
        partes = [p for p in (self.tratamento, self.arroba) if p]
        return " ".join(partes)

    def gerar_lote(self, quantidade=50):
        quantidade = max(1, min(int(quantidade), 200))
        combinacoes = []

        if self.texto_base:
            combinacoes.append(self.texto_base)

        if self.destinatario:
            aberturas = [
                ab.format(destinatario=self.destinatario)
                for ab in self.ABERTURAS_COM_DESTINATARIO
            ]
        else:
            aberturas = list(self.ABERTURAS_NEUTRAS)

        pool = [
            f"{ab} {nuc} {ch} {self.hashtag}".strip()
            for ab in aberturas
            for nuc in self.NUCLEOS
            for ch in self.CHAMADAS
        ]
        random.shuffle(pool)

        for idx, corpo in enumerate(pool):
            if len(combinacoes) >= quantidade:
                break
            topo, base = self.MOLDURAS_EMOJI[idx % len(self.MOLDURAS_EMOJI)]
            msg_final = f"{topo}\n{corpo}\n{base}"
            if msg_final not in combinacoes:
                combinacoes.append(msg_final)

        return combinacoes


def gerar_lote_impulsionamento(texto_base, quantidade=50, arroba_custom="", hashtag_custom="", tratamento=""):
    motor = MotorImpulsionamento(
        texto_base=texto_base,
        arroba_custom=arroba_custom,
        hashtag_custom=hashtag_custom,
        tratamento=tratamento,
    )
    return motor.gerar_lote(quantidade=quantidade)
