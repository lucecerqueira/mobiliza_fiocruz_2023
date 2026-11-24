from django import forms


class ImpulsionamentoForm(forms.Form):
    post_url = forms.URLField(
        label="Link do Post Alvo (Instagram / X / TikTok)",
        initial="https://www.instagram.com/p/DgFYs8wFmlV/",
        widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "https://www.instagram.com/p/..."}),
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
        label="Texto Base (Modelo de referência — opcional)",
        required=False,
        initial=(
            "🇧🇷‼️🇧🇷🇧🇷🇧🇷🇧🇷‼️🇧🇷🇧🇷🇧🇷‼️🇧🇷‼️\n"
            "@belchiormiriam, a Fiocruz é essencial para o SUS e suas pesquisas impactam diretamente "
            "a vida das pessoas. Convoque os excedentes do último concurso: são centenas de profissionais "
            "qualificados prontos para somar ao SUS! #ConvocaFiocruz\n"
            "🇧🇷‼️🇧🇷🇧🇷🇧🇷🇧🇷‼️🇧🇷🇧🇷🇧🇷‼️🇧🇷‼️"
        ),
        widget=forms.Textarea(attrs={"rows": 5, "class": "form-control"}),
    )
