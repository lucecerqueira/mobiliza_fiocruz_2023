# Mobiliza Fiocruz 2023

Plataforma independente de participação cidadã. Não representa oficialmente a Fiocruz nem o Governo Federal.

## Requisitos
- Linux Mint
- Python 3.12
- PostgreSQL 14 ou superior

## 1. Criar ambiente virtual
```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 2. PostgreSQL
Crie banco e usuário (ajuste a senha):
```bash
sudo -u postgres psql
```
No prompt SQL:
```sql
CREATE USER mobiliza WITH PASSWORD 'troque-esta-senha';
CREATE DATABASE mobiliza_fiocruz OWNER mobiliza;
\q
```

## 3. Configuração
```bash
cp .env.example .env
nano .env
```
Defina `DJANGO_SECRET_KEY`, senha do banco e, quando escolher o provedor, `AI_API_URL`, `AI_API_KEY` e `AI_MODEL`.

O serviço de IA usa formato compatível com Chat Completions. Não coloque a chave no código nem no Git.

## 4. Inicialização
```bash
python manage.py check
python manage.py makemigrations usuarios campanhas publicacoes conteudos mobilizacao monitoramento
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Acesse:
- Aplicação: http://127.0.0.1:8000/
- Administração: http://127.0.0.1:8000/admin/

## 5. Primeiro uso
1. Entre em `/admin/`.
2. Cadastre uma campanha.
3. Cadastre temas e conteúdos.
4. Cadastre links de publicações oficiais.
5. Cadastre tarefas voluntárias.
6. Crie usuário de teste pela tela de cadastro.

## Observações
- A API de IA ainda depende da escolha de um provedor e modelo.
- O projeto não publica automaticamente em Instagram ou TikTok.
- O painel exibe contagens do banco, não métricas reais das redes.
- Antes de disponibilizar publicamente, revisar política de privacidade, termos de uso, segurança, permissões e política de retenção de dados.
- Em produção, configurar HTTPS, `DEBUG=False`, `ALLOWED_HOSTS`, cookies seguros, backups e envio de e-mail para recuperação de senha.
