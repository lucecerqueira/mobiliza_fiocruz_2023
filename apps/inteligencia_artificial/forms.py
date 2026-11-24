from django import forms


class ImpulsionamentoForm(forms.Form):
    post_url = forms.URLField(
        label="Link do Post Alvo (Instagram / X / TikTok)",
        initial="https://www.instagram.com/p/DgFYs8wFmlV/",
        widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "https://www.instagram.com/p/..."}),
    )
    estilo = forms.ChoiceField(
        label="Estilo dos textos",
        choices=[
            ("misto", "Misto (Recomendado — Anti-spam)"),
            ("curto", "Curto e direto"),
            ("pergunta", "Pergunta direta (gera respostas)"),
            ("impacto", "Impacto concreto no SUS"),
            ("institucional", "Institucional / técnico"),
        ],
        initial="misto",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    tratamento = forms.CharField(
        max_length=60,
        required=False,
        initial="",
        label="Cargo / Tratamento (opcional)",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "list": "opcoes-tratamento",
                "placeholder": "Ex: Ministra, Ministro, Presidente (ou vazio)",
            }
        ),
    )
    arroba_alvo = forms.CharField(
        max_length=80,
        required=False,
        initial="@belchiormiriam",
        label="Perfil marcado (@)",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "@perfil ou deixe vazio"}),
    )
    hashtag = forms.CharField(
        max_length=80,
        required=False,
        initial="#ConvocaFiocruz",
        label="Hashtag da campanha (#)",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    quantidade = forms.ChoiceField(
        label="Quantidade de variações",
        choices=[
            ("20", "20 variações"),
            ("50", "50 variações"),
            ("100", "100 variações"),
            ("200", "200 variações"),
        ],
        initial="200",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    texto_base = forms.CharField(
        label="Texto Base (opcional — incluído como variação #1 se preenchido)",
        required=False,
        initial=(
            "@belchiormiriam, a Fiocruz é essencial para o SUS e suas pesquisas impactam diretamente "
            "a vida das pessoas. Convoque todos os excedentes do último concurso: são centenas de "
            "profissionais qualificados prontos para somar ao SUS! #ConvocaFiocruz"
        ),
        widget=forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
    )
