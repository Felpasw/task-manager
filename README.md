GRUPO: 
  Felipe Cavalcante Lacerda <br/>
  Pedro Henrique Mazzeu Sá

# Como Rodar a Aplicação

Este guia fornece um passo a passo para rodar a aplicação localmente.

## Pré-requisitos

- Python 3.x instalado (verifique rodando `python3 --version` ou `python --version` no Windows)
- Django configurado corretamente no seu ambiente (instale com `pip install django` se necessário)

## Passos para executar a aplicação

### 1. Abrir o Terminal

Abra o terminal ou prompt de comando e navegue até a pasta onde o projeto está localizado.

cd caminho/para/seu/projeto

### 2. Executar as Migrações do Banco de Dados

Para aplicar as migrações e configurar o banco de dados, execute o seguinte comando:

- **Linux/macOS**:

  python3 manage.py migrate

- **Windows**:

  python manage.py migrate

Esse comando cria as tabelas necessárias no banco de dados.

### 3. Criar um Superusuário

Após as migrações, crie um superusuário para acessar o painel de administração da aplicação:

- **Linux/macOS**:

  python3 manage.py createsuperuser

- **Windows**:

  python manage.py createsuperuser

Siga as instruções para definir o nome de usuário, e-mail e senha.

### 4. Executar o Servidor de Desenvolvimento

Agora, execute o servidor de desenvolvimento para iniciar a aplicação localmente:

- **Linux/macOS**:

  python3 manage.py runserver

- **Windows**:

  python manage.py runserver

O servidor será iniciado no endereço padrão: http://127.0.0.1:8000.

### 5. Acessar a Aplicação

Abra um navegador e acesse http://127.0.0.1:8000 para ver a aplicação rodando. Você pode acessar o painel administrativo em http://127.0.0.1:8000/admin com o usuário que você criou no passo 3.

## Resumo de Comandos

- Linux/macOS:

  python3 manage.py migrate
  python3 manage.py createsuperuser
  python3 manage.py runserver

- Windows:

  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver

Pronto! Agora você já pode acessar e utilizar a aplicação.
