# config.py
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


# Configurações do banco de dados
class Config:
    SQLALCHEMY_DATABASE_PORT = os.getenv('SQLALCHEMY_DATABASE_PORT')
    SQLALCHEMY_DATABASE_HOST = os.getenv('SQLALCHEMY_DATABASE_HOST')
    SQLALCHEMY_DATABASE_NAME = os.getenv('SQLALCHEMY_DATABASE_NAME')
    SQLALCHEMY_DATABASE_USER = os.getenv('SQLALCHEMY_DATABASE_USER')
    SQLALCHEMY_DATABASE_PASSWORD = os.getenv('SQLALCHEMY_DATABASE_PASSWORD')
