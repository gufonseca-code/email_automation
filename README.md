# Email Automation

Guia rápido para clonar, configurar e executar este projeto (Python/Flask).

## Pré-requisitos

- Git
- Python 3.8+ instalado
- Pip (vem com Python)

## Clonar o repositório

Substitua o URL pelo repositório real.

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

## Criar e ativar ambiente virtual

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
```

Windows (CMD):

```cmd
python -m venv venv
venv\\Scripts\\activate.bat
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Arquivo de configuração (.env)

O projeto usa `python-dotenv`. Crie um arquivo `.env` na raiz com as variáveis abaixo (substitua pelos seus valores):

```env
SMTP_SERVER=smtp.exemplo.com
SMTP_PORT=587
EMAIL_ADDRESS=seu-email@exemplo.com
EMAIL_PASSWORD=sua_senha_de_email
# Opcional: URL do banco de dados (ex: postgres, mysql). Se não informado, usa sqlite local
DATABASE_URL=sqlite:///email_automation.db
```

Atenção: no `app/config.py` estas variáveis são usadas por `Config`.

## Migrações (banco de dados)

Se desejar aplicar migrações existentes, use `flask` com `FLASK_APP` apontando para `run.py`.

Linux / macOS:

```bash
export FLASK_APP=run.py
flask db upgrade
```

Windows (PowerShell):

```powershell
$env:FLASK_APP = "run.py"
flask db upgrade
```

Windows (CMD):

```cmd
set FLASK_APP=run.py
flask db upgrade
```

> Observação: o projeto já contém a pasta `migrations`. Se preferir, pode ignorar migrações e usar o banco sqlite local padrão.

## Executar a aplicação

Modo rápido (script principal):

```bash
python run.py
```

Ou via CLI do Flask:

Linux / macOS:

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

Windows (PowerShell):

```powershell
$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"
flask run
```

Windows (CMD):

```cmd
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

A aplicação por padrão roda em `http://127.0.0.1:5000`.

## Teste de envio de e-mail

Antes de enviar e-mails, verifique as variáveis SMTP em `.env`. O serviço de e-mail do projeto usa as variáveis `SMTP_SERVER`, `SMTP_PORT`, `EMAIL_ADDRESS` e `EMAIL_PASSWORD`.

## Gerar passkeys / senhas de app (Gmail e Outlook)

Alguns provedores (como Google e Microsoft) exigem que você gere uma senha de aplicativo (chamada aqui de "passkey") quando usa autenticação em apps que não suportam OAuth. Abaixo estão os passos gerais para gerar essas senhas e usá-las em `.env` como `EMAIL_PASSWORD`.

- **Observação importante:** ative a autenticação em dois fatores (2-Step Verification / Verificação em duas etapas) na sua conta antes de criar uma senha de app.

- Gmail (Conta Google):
	1. Acesse sua Conta Google: clique em `Gerenciar sua conta do Google`.
 2. Vá em `Segurança` -> `Verificação em duas etapas` e ative-a (se ainda não estiver ativa).
 3. Depois de ativar, em `Segurança` procure por `Senhas de app` (ou `App passwords`).
 4. Clique em `Selecionar app` escolha `Mail` e em `Selecionar dispositivo` escolha um nome (ou `Other` e informe um nome legível).
 5. Clique em `Gerar`. O Google mostrará uma senha de 16 caracteres (sem espaços).
 6. Copie essa senha e cole no seu arquivo `.env` em `EMAIL_PASSWORD` (substituindo a senha da conta).
 7. Use também `SMTP_SERVER=smtp.gmail.com` e `SMTP_PORT=587` (TLS) no `.env`.

- Outlook / Conta Microsoft (Outlook.com, Hotmail, Live, ou Microsoft 365):
	1. Entre na sua conta Microsoft e acesse `Segurança` (Security) ou `Informações de segurança`.
	2. Ative a verificação em duas etapas (se ainda não estiver ativa).
	3. Vá para `Opções avançadas de segurança` ou `More security options`.
	4. Procure por `Senhas de aplicativo` (App passwords) e clique em `Criar uma nova senha de aplicativo`.
	5. Será gerada uma senha; copie-a imediatamente.
	6. Cole essa senha no seu `.env` em `EMAIL_PASSWORD`.
	7. Para servidores SMTP use `SMTP_SERVER=smtp.office365.com` e `SMTP_PORT=587` (TLS). Para algumas contas Outlook.com também funciona `smtp-mail.outlook.com`.

- Uso no projeto: no `.env` coloque as variáveis necessárias, por exemplo:

```env
EMAIL_ADDRESS=seu-email@exemplo.com
EMAIL_PASSWORD=senha_de_app_gerada_pelo_provedor
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

- Segurança: nunca commit o `.env` nem compartilhe a senha de app. Use `.gitignore` (já presente) para evitar o envio acidental.

Se precisar, eu posso adicionar um arquivo `.env.example` com os nomes das variáveis (sem valores) para facilitar a configuração por outros usuários.

## Problemas comuns

- Erro sobre `SMTP_PORT` vazio: verifique se `SMTP_PORT` está definida no `.env` (deve ser um número).
- Dependências: confirme que o `venv` está ativado antes de instalar ou executar.

## Windows vs macOS/Linux — resumo rápido

- Ativar venv: `source venv/bin/activate` (macOS/Linux) vs `venv\\Scripts\\activate.bat` ou `Activate.ps1` (Windows).
- Export de variáveis de ambiente: `export VAR=valor` (macOS/Linux) vs `$env:VAR = "valor"` (PowerShell) vs `set VAR=valor` (CMD).

---
