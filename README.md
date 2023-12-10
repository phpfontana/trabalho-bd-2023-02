# Trabalho Banco de Dados - 2023/02

Este repositório contém o trabalho da disciplina de Banco de Dados.

## Setup
1. Instale PostgreSQL seguindo as instruções do site oficial:
    - [PostgreSQL](https://www.postgresql.org/download/)
2. Instale as dependências do projeto com o comando:
    
    ```bash 
    pip install -r requirements.txt
    ```
3. Crie um arquivo `.env` na raiz do projeto com as seguintes credenciais de ambiente:
    ```bash
    SQLALCHEMY_DATABASE_HOST=YOUR_HOST
    SQLALCHEMY_DATABASE_PORT=YOUR_PORT
    SQLALCHEMY_DATABASE_NAME=YOUR_DATABASE_NAME
    SQLALCHEMY_DATABASE_USER=YOUR_USER
    SQLALCHEMY_DATABASE_PASSWORD=YOUR_PASSWORD
    ```
   
## Execução
1. Execute o comando abaixo para criar as tabelas e popular o seu banco de dados:
    ```bash
    python init_db.py
    ```