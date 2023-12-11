import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


from config import Config


# Cria o engine de conexão com o banco de dados
def get_engine(user, password, host, port, db):
    # Cria o engine de conexão com o banco de dados
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"

    # Verifica se o banco de dados existe, caso não exista, cria o banco de dados
    if not database_exists(url):
        create_database(url)
        print(f"Banco de dados {db} criado com sucesso!")

    # Cria o engine de conexão com o banco de dados
    engine = create_engine(url, echo=False, pool_size=50)

    return engine


def get_engine_from_config():
    return get_engine(
        Config.SQLALCHEMY_DATABASE_USER,
        Config.SQLALCHEMY_DATABASE_PASSWORD,
        Config.SQLALCHEMY_DATABASE_HOST,
        Config.SQLALCHEMY_DATABASE_PORT,
        Config.SQLALCHEMY_DATABASE_NAME
    )


def get_session():
    engine = get_engine_from_config()
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


def login():
    from app.controller.UsuarioController import UsuarioController
    print("Bem-vindo ao Sistema de Gerenciamento da Biblioteca")
    username = input('Nome de Usuário: ')
    password = input('Senha: ')

    usuario = UsuarioController.buscar_usuario_por_nome(username)

    if usuario and usuario.senha == password:  # Aqui deve-se implementar uma verificação de hash de senha
        print(f"Bem-vindo, {usuario.nickname}!")
        return usuario
    else:
        print("Usuário ou senha incorretos!")
        return None


