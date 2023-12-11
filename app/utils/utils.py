import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from app.controller.AlunoController import AlunoController
from app.controller.EmprestimoController import EmprestimosController
from app.controller.FuncionarioController import FuncionarioController
from app.controller.ProfessorController import ProfessorController
from app.controller.UsuarioController import UsuarioController
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


def criar_aluno(nickname, senha, matricula, permissao, data_ingresso, data_previsao_conclusao, curso_descricao):
    AlunoController.criar_aluno(nickname, senha, matricula, permissao, data_ingresso, data_previsao_conclusao,
                                curso_descricao)


def criar_professor(nickname, senha, matricula, permissao, data_contratacao, regime_trabalho, curso_descricao):

    ProfessorController.criar_professor(nickname, senha, matricula, permissao, data_contratacao, regime_trabalho,
                                        curso_descricao)


def criar_funcionario(nickname, senha, matricula, permissao, data_contratacao):

    FuncionarioController.criar_funcionario(nickname, senha, matricula, permissao, data_contratacao)


def criar_emprestimo(status_emprestimo, data_emprestimo, data_devolucao, usuario_id, livro_id):

    EmprestimosController.criar_emprestimo(status_emprestimo, data_emprestimo, data_devolucao, usuario_id, livro_id)

