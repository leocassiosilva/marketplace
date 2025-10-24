# Marketplace de Autopeças

Este projeto é um **Marketplace de Autopeças** desenvolvido em **Django**, com as seguintes funcionalidades:

- Listar peças disponíveis no estoque.  
- Visualizar detalhes de cada peça (nome, descrição, preço, quantidade disponível).  
- Apenas usuários administradores podem cadastrar, editar ou remover peças.  

O sistema é pensado para facilitar o gerenciamento de estoque e permitir que os administradores popularem rapidamente o banco de dados a partir de planilhas, enquanto usuários comuns podem apenas consultar os produtos.

---

## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- **Python 3.10 ou superior**  
- **pip** (gerenciador de pacotes do Python)  
- **PostgreSQL** (ou outro banco de dados configurado no projeto)  
- **Git**  

---

### 1. Clonar o Repositório

Clone o repositório oficial do projeto e entre na pasta:

```bash
git clone https://github.com/leocassiosilva/marketplace.git
cd marketplace
```
### 2. Criar o Ambiente Virtual

1. Navegue até o diretório onde deseja criar o ambiente virtual.
2. Execute o comando abaixo para criar o ambiente virtual:

   **Linux ou macOS:**
     ```bash
     python3 -m venv nome_do_ambiente
     ```
   **Windows:**
    ```bash
    python -m venv nome_do_ambiente
    ```
    Após a criação, você provavelmente já estará no ambiente virtual.

### 3. Ativar o Ambiente Virtual
1. Execute o comando abaixo para ativar o ambiente virtual:

   **Linux ou macOS:**
     ```bash
     source nome_do_ambiente/bin/activate
     ```
   **Windows:**
    ```bash
    .\nome_do_ambiente\Scripts\activate
    ```

### 4. Instalar as Dependências
1. Execute o comando abaixo para ativar o ambiente virtual:
     ```bash
     pip install -r requirements.txt
     ```
### 5. Criar o Banco de Dados
No seu projeto Django, a configuração do banco de dados já está pronta no arquivo settings.py, e você só precisa criar o arquivo .env com as variáveis de ambiente necessárias. Esse arquivo deve conter as informações de configuração do banco de dados e outras configurações sensíveis.

```bash
  SECRET_KEY=your_secret_key
  DEBUG=True
  PASSWORD_POSTGRES='sua_senha'
  USER_POSTGRES='seu_user'
  DATABASE_POSTGRES='seu_banco'
  HOST_POSTGRES='localhost'
  PORT_POSTGRES='5432'
  DEV=False
```
### 6. Executar as Migrações
```bash
  python manage.py migrate
```
### 7. Executar o Projeto
Agora você pode rodar o servidor de desenvolvimento do Django:
```bash
  python manage.py runserver
```
Neste momento seu banco estará sem nenhhum usuário cadastrado. O sistema conta com cadastro pela interface, mas, caso queira, é possível criar um usuário pela linha de comando. Basta executar este comando e informar o que for pedido:
```bash
python manage.py createuser
```

Acesse a aplicação em: http://127.0.0.1:8000
A interface administrativa está em: http://127.0.0.1:8000/admin
