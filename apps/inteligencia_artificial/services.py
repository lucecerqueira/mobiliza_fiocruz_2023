import random
import re


class MotorImpulsionamento:
    ESTILOS_VALIDOS = ("misto", "curto", "pergunta", "impacto", "institucional")
    PROPRIOS_MAIUSCULOS = {"Fiocruz", "SUS", "Brasil"}

    CURTO_ABERTURAS = [
        "O concurso da Fiocruz já está pronto e homologado.",
        "Centenas de cientistas e técnicos já foram aprovados na Fiocruz.",
        "O SUS precisa de reforço imediato na Fiocruz.",
        "A Fiocruz tem aprovados prontos para começar a trabalhar hoje.",
        "Vacinas, exames e pesquisa dependem de gente na Fiocruz.",
        "Não faz sentido deixar aprovados na Fiocruz parados enquanto falta gente no SUS.",
        "O concurso Fiocruz 2023 foi rigoroso e aprovou profissionais de ponta.",
        "Saúde pública forte exige a Fiocruz com equipe completa.",
        "A ciência brasileira precisa de reforço agora na Fiocruz.",
        "O Brasil já investiu na seleção desses profissionais da Fiocruz.",
        "A Fiocruz salva vidas todos os dias, mas precisa de mais servidores.",
        "Tem profissional qualificado e aprovado esperando para servir ao SUS na Fiocruz.",
        "Mais gente na Fiocruz significa mais saúde na ponta.",
        "O concurso já aconteceu e a demanda do SUS é urgente.",
        "Valorizar o SUS é colocar quem foi aprovado na Fiocruz para trabalhar.",
    ]

    CURTO_FECHAMENTOS = [
        "Só falta autorizar a chamada de todos os excedentes!",
        "Convoque todos os excedentes já!",
        "Autorize a nomeação de todos os excedentes agora!",
        "Chamem todos os excedentes do concurso 2023!",
        "É hora de nomear todos os excedentes!",
        "Libere a convocação de todos os excedentes!",
        "Convoquem todos os excedentes e fortaleçam o SUS!",
        "A chamada de todos os excedentes não pode esperar!",
        "Coloque todos os excedentes para trabalhar pela saúde pública!",
        "Nomeação de todos os excedentes já!",
        "Dê o sinal verde para chamar todos os excedentes!",
        "Autorizem a entrada de todos os excedentes da Fiocruz!",
        "Não deixem ninguém de fora: chamem todos os excedentes!",
        "Convoque todos os aprovados excedentes agora!",
        "O SUS conta com a convocação de todos os excedentes!",
    ]

    PERGUNTA_ABERTURAS = [
        "Por que deixar centenas de aprovados na Fiocruz esperando enquanto o SUS precisa de reforço?",
        "Quando sai a autorização para reforçar a equipe da Fiocruz com o concurso 2023?",
        "O concurso já está homologado e o SUS precisa de gente: o que falta para agir?",
        "Como ampliar a produção de vacinas e pesquisas no Brasil sem reforçar a Fiocruz?",
        "Por que desperdiçar cientistas e técnicos já selecionados em concurso público?",
        "Até quando profissionais prontos para servir ao SUS vão ficar esperando em casa?",
        "Com tanta demanda na saúde pública, por que manter a Fiocruz com equipe reduzida?",
        "Qual é o prazo para o governo liberar as novas nomeações da Fiocruz?",
        "O Brasil já investiu em um concurso rigoroso na Fiocruz — por que não aproveitar quem passou?",
        "Como enfrentar novas epidemias e ampliar pesquisas sem mais servidores na Fiocruz?",
        "Por que deixar laboratórios e unidades sobrecarregados se há aprovados prontos para assumir?",
        "Se o SUS é prioridade, o que impede a entrada imediata de novos servidores na Fiocruz?",
        "Quem ganha com especialistas aprovados esperando enquanto a saúde pública precisa deles?",
        "Vacina, pesquisa e atendimento no SUS podem esperar?",
        "Quando a Fiocruz vai receber o reforço que a população brasileira precisa?",
    ]

    PERGUNTA_FECHAMENTOS = [
        "Chamem todos os excedentes da Fiocruz!",
        "Convoquem todos os excedentes já!",
        "A resposta é simples: nomeiem todos os excedentes!",
        "Autorizem a chamada de todos os excedentes agora!",
        "O SUS precisa da convocação de todos os excedentes!",
        "Libere a nomeação de todos os excedentes do concurso 2023!",
        "Não desperdice talentos: convoque todos os excedentes!",
        "Hora de chamar todos os excedentes da Fiocruz!",
        "A saúde pública agradece a convocação de todos os excedentes!",
        "Coloquem todos os excedentes para trabalhar pelo Brasil!",
        "Autorize todos os excedentes da Fiocruz já!",
        "Garanta a entrada de todos os aprovados excedentes!",
        "Convoque todos os excedentes e fortaleça a ciência!",
        "Queremos a nomeação de todos os excedentes!",
        "Dê o passo certo: convoque todos os excedentes!",
    ]

    IMPACTO_ABERTURAS = [
        "Vacina no posto, remédio gratuito e pesquisa contra doenças dependem de gente trabalhando na Fiocruz.",
        "Quem usa o SUS sabe o quanto o trabalho da Fiocruz faz diferença no dia a dia das famílias.",
        "Por trás de cada vacina e diagnóstico no SUS existem profissionais dedicados na Fiocruz.",
        "Dengue, câncer, doenças raras e novas epidemias exigem laboratórios da Fiocruz funcionando a todo vapor.",
        "Produzir medicamentos e vacinas aqui no Brasil reduz custos e salva vidas na ponta.",
        "A saúde da população melhora quando a Fiocruz tem equipe completa para pesquisar e produzir.",
        "Sem mais gente nos laboratórios e unidades da Fiocruz, quem sente na pele é quem depende do SUS.",
        "Cada mês sem nomeação é pesquisa atrasada e menos capacidade de resposta para a saúde pública.",
        "Investir em quem faz ciência na Fiocruz é investir direto na proteção de milhões de brasileiros.",
        "Do atendimento especializado à fabricação de vacinas, a Fiocruz está presente na vida de todo brasileiro.",
        "Fortalecer a Fiocruz não é gasto: é garantir vacina, remédio e cuidado gratuito para quem precisa.",
        "O Brasil tem especialistas prontos para acelerar pesquisas e ampliar entregas no SUS.",
        "Cuidar da saúde pública de verdade significa colocar mais gente qualificada para atuar na Fiocruz.",
        "A população precisa de um SUS mais rápido, mais forte e com a Fiocruz trabalhando com força total.",
        "Pesquisa de ponta e vacina gratuita no braço da população só acontecem com servidores na Fiocruz.",
    ]

    IMPACTO_FECHAMENTOS = [
        "Convocar todos os excedentes do concurso 2023 é investir direto na saúde da população!",
        "Autorize a chamada de todos os excedentes e fortaleça o SUS na ponta!",
        "Nomear todos os excedentes da Fiocruz significa mais vacinas e mais pesquisa para o Brasil!",
        "Convoque todos os excedentes: é reforço imediato para quem depende do SUS!",
        "Chamar todos os excedentes da Fiocruz traz resultado rápido para milhões de pessoas!",
        "Libere a nomeação de todos os excedentes e coloque a ciência brasileira para avançar!",
        "A convocação de todos os excedentes garante mais entregas reais para a saúde pública!",
        "Nomeie todos os excedentes do último concurso: o Brasil inteiro ganha com isso!",
        "Autorize todos os excedentes da Fiocruz e reforce quem cuida da nossa saúde!",
        "Convoque todos os aprovados excedentes para ampliar o alcance do SUS!",
        "A chamada de todos os excedentes é o caminho mais rápido para fortalecer a Fiocruz!",
        "Garanta a entrada de todos os excedentes e proteja o futuro da saúde pública!",
        "Convoque todos os excedentes já: a população brasileira precisa desse reforço!",
        "Não deixe esses profissionais esperando — autorize a nomeação de todos os excedentes!",
        "Fortaleça a saúde de todo o país com a convocação de todos os excedentes da Fiocruz!",
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
        "Defender a saúde pública é defender o fortalecimento imediato da Fiocruz.",
        "A ciência brasileira avança quando a Fiocruz conta com equipe completa.",
        "Produção nacional de vacinas, fármacos e pesquisa exige uma Fiocruz fortalecida.",
        "Valorizar o serviço público de saúde passa pela ampliação do quadro da Fiocruz.",
        "O Brasil inteiro se beneficia do trabalho científico e tecnológico da Fiocruz.",
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
        "Os aprovados em cadastro de reserva representam reforço imediato e qualificado para o país.",
        "O concurso 2023 selecionou profissionais de alto nível que podem dar resposta rápida à demanda do SUS.",
        "A ampliação do quadro efetivo garante continuidade a projetos estratégicos de saúde pública.",
        "Esses candidatos já passaram por seleção rigorosa e estão prontos para servir à população.",
        "Aproveitar o certame vigente evita a perda de talentos essenciais para a ciência nacional.",
        "Com a equipe recomposta, a instituição amplia sua capacidade de resposta a emergências sanitárias.",
    ]

    CHAMADAS = [
        "Convoque todos os excedentes do último concurso: são centenas de profissionais qualificados prontos para somar ao SUS!",
        "Autorize a convocação de todos os excedentes do concurso Fiocruz 2023 agora!",
        "Libere a nomeação de todos os aprovados excedentes e fortaleça o SUS!",
        "Convoque todos os excedentes aprovados! O Brasil precisa desses profissionais atuando na saúde pública.",
        "Dê o próximo passo pelo fortalecimento do SUS e autorize a chamada de todos os excedentes da Fiocruz!",
        "Nomeie todos os excedentes do último certame: a saúde pública brasileira agradece!",
        "Autorize a convocação imediata de todos os excedentes aprovados no concurso da Fiocruz!",
        "Convoque todos os aprovados excedentes e garanta mais força de trabalho para a ciência nacional!",
        "O SUS precisa desses especialistas! Autorize a convocação de todos os excedentes da Fiocruz.",
        "Chamada de todos os excedentes já! Profissionais prontos para servir ao SUS e à ciência.",
        "Garanta a nomeação de todos os excedentes da Fiocruz e reforce a pesquisa pública no Brasil!",
        "Convoque todos os excedentes do concurso 2023! A população brasileira precisa desse reforço no SUS.",
        "Não deixe nenhum aprovado de fora: autorize a convocação de todos os excedentes da Fiocruz!",
        "Fortaleça a ciência e a vigilância em saúde com a chamada de todos os excedentes aprovados!",
        "A hora é agora: autorize a nomeação de todos os excedentes do concurso da Fiocruz!",
    ]

    SUFIXOS_LIMPOS = ["", "", "", " 🇧🇷", " 🔬", " 🏥"]
    PREFIXOS_LEVES = ["🔬 ", "📢 ", "💉 ", "🏥 ", "🇧🇷 ", "⚡ "]
    MOLDURAS_EMOJI = [
        ("🇧🇷‼️🇧🇷🇧🇷🇧🇷🇧🇷‼️🇧🇷🇧🇷🇧🇷‼️🇧🇷‼️", "🇧🇷‼️🇧🇷🇧🇷🇧🇷🇧🇷‼️🇧🇷🇧🇷🇧🇷‼️🇧🇷‼️"),
        ("🚨🇧🇷🚨🇧🇷🚨🇧🇷🚨🇧🇷🚨", "🚨🇧🇷🚨🇧🇷🚨🇧🇷🚨🇧🇷🚨"),
        ("🇧🇷📢🇧🇷📢🇧🇷📢🇧🇷", "🇧🇷📢🇧🇷📢🇧🇷📢🇧🇷"),
        ("‼️🇧🇷‼️🇧🇷‼️🇧🇷‼️", "‼️🇧🇷‼️🇧🇷‼️🇧🇷‼️"),
        ("🇧🇷🔬🇧🇷💉🇧🇷🏥🇧🇷", "🇧🇷🔬🇧🇷💉🇧🇷🏥🇧🇷"),
        ("⚡🇧🇷⚡🇧🇷⚡🇧🇷⚡", "⚡🇧🇷⚡🇧🇷⚡🇧🇷⚡"),
    ]

    def __init__(self, texto_base="", arroba_custom="", hashtag_custom="", tratamento="", estilo="misto"):
        self.texto_base = (texto_base or "").strip()
        self.arroba = self._resolver_arroba(arroba_custom)
        self.hashtag = self._resolver_hashtag(hashtag_custom)
        self.tratamento = (tratamento or "").strip()
        self.destinatario = self._montar_destinatario()
        self.estilo = estilo if estilo in self.ESTILOS_VALIDOS else "misto"

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
        return " ".join(p for p in (self.tratamento, self.arroba) if p)

    def _minuscula_inicial(self, texto):
        if not texto:
            return texto
        primeira_palavra = texto.split()[0].strip(".,!?:;—-")
        if primeira_palavra in self.PROPRIOS_MAIUSCULOS:
            return texto
        return texto[0].lower() + texto[1:]

    def _incorporar_destinatario_e_hashtag(self, corpo, idx):
        if not self.destinatario:
            return f"{corpo} {self.hashtag}".strip()
        # Quando só há @ (sem cargo), alterna menção no início e no fim para soar mais orgânico
        if not self.tratamento and idx % 3 == 2:
            return f"{corpo} {self.destinatario} {self.hashtag}".strip()
        return f"{self.destinatario}, {self._minuscula_inicial(corpo)} {self.hashtag}".strip()

    def _aplicar_formato_emoji(self, texto, idx):
        # Distribuição equilibrada a cada 10 itens: 5 limpos (50%), 3 leves (30%), 2 molduras (20%)
        slot = idx % 10
        if slot < 5:
            sufixo = self.SUFIXOS_LIMPOS[idx % len(self.SUFIXOS_LIMPOS)]
            return f"{texto}{sufixo}"
        if slot < 8:
            prefixo = self.PREFIXOS_LEVES[idx % len(self.PREFIXOS_LEVES)]
            return f"{prefixo}{texto}"
        topo, base = self.MOLDURAS_EMOJI[idx % len(self.MOLDURAS_EMOJI)]
        return f"{topo}\n{texto}\n{base}"

    def _gerar_pool_estilo(self, estilo):
        if estilo == "curto":
            pool = [f"{a} {f}" for a in self.CURTO_ABERTURAS for f in self.CURTO_FECHAMENTOS]
        elif estilo == "pergunta":
            pool = [f"{a} {f}" for a in self.PERGUNTA_ABERTURAS for f in self.PERGUNTA_FECHAMENTOS]
        elif estilo == "impacto":
            pool = [f"{a} {f}" for a in self.IMPACTO_ABERTURAS for f in self.IMPACTO_FECHAMENTOS]
        else:
            pool = [
                f"{ab} {nuc} {ch}"
                for ab in self.ABERTURAS_NEUTRAS
                for nuc in self.NUCLEOS
                for ch in self.CHAMADAS
            ]
        random.shuffle(pool)
        return pool

    def gerar_lote(self, quantidade=50):
        quantidade = max(1, min(int(quantidade), 200))
        combinacoes = []

        if self.texto_base:
            combinacoes.append(self.texto_base)

        restante = quantidade - len(combinacoes)
        if restante <= 0:
            return combinacoes[:quantidade]

        if self.estilo == "misto":
            estilos = ("curto", "pergunta", "impacto", "institucional")
            pools = {est: self._gerar_pool_estilo(est) for est in estilos}
            selecionados = []
            idx_estilo = 0
            while len(selecionados) < restante * 2:
                est = estilos[idx_estilo % len(estilos)]
                idx_estilo += 1
                if pools[est]:
                    selecionados.append(pools[est].pop())
                if all(not p for p in pools.values()):
                    break
        else:
            selecionados = self._gerar_pool_estilo(self.estilo)

        # Embaralha os formatos de emoji mantendo a proporção 50/30/20
        indices_formato = list(range(len(selecionados)))
        random.shuffle(indices_formato)

        for pos, corpo in enumerate(selecionados):
            if len(combinacoes) >= quantidade:
                break
            texto_com_alvo = self._incorporar_destinatario_e_hashtag(corpo, pos)
            msg_final = self._aplicar_formato_emoji(texto_com_alvo, indices_formato[pos])
            if msg_final not in combinacoes:
                combinacoes.append(msg_final)

        return combinacoes


def gerar_lote_impulsionamento(
    texto_base,
    quantidade=50,
    arroba_custom="",
    hashtag_custom="",
    tratamento="",
    estilo="misto",
):
    motor = MotorImpulsionamento(
        texto_base=texto_base,
        arroba_custom=arroba_custom,
        hashtag_custom=hashtag_custom,
        tratamento=tratamento,
        estilo=estilo,
    )
    return motor.gerar_lote(quantidade=quantidade)
