from sqlalchemy_utils import database_exists, create_database, drop_database
from app.model.models import Base, Autor, Livro, Usuario, AutoresDosLivros
from app.utils.utils import get_engine_from_config, get_session


def reset_database():
    engine = get_engine_from_config()

    # Exclui o banco de dados se ele já existir
    if database_exists(engine.url):
        print(f"Excluindo o banco de dados existente: {engine.url}")
        drop_database(engine.url)

    # Cria o banco de dados
    print(f"Criando o banco de dados: {engine.url}")
    create_database(engine.url)

    # Cria todas as tabelas definidas nos modelos
    Base.metadata.create_all(engine)


def main():
    reset_database()

    session = get_session()

    # Insira autores
    autores = [
        Autor(nome='Machado de Assis', cpf='11122233344', nacionalidade='Brasileira'),
        Autor(nome='Clarice Lispector', cpf='22233344455', nacionalidade='Brasileira'),
        # Adicione os demais autores aqui
    ]
    session.add_all(autores)

    # Insira livros
    livros = [
        Livro(titulo='Dom Casmurro', ISBN='ISBN12345', ano=1899, editora='Editora A', quantidade=5,
              Categoria='Romance'),
        Livro(titulo='A Hora da Estrela', ISBN='ISBN23456', ano=1977, editora='Editora B', quantidade=3,
              Categoria='Romance'),
        # Adicione os demais livros aqui
    ]
    session.add_all(livros)

    # Insira usuário
    usuario = Usuario(nickname='admin', senha='123456', matricula='123456', permissao='admin')
    session.add(usuario)

    session.commit()

    # Associações de autores com livros
    associacoes = [
        AutoresDosLivros(Autores_id_autor=1, Livros_idLivros=1),
        AutoresDosLivros(Autores_id_autor=2, Livros_idLivros=2),
        # Adicione as demais associações aqui
    ]
    session.add_all(associacoes)

    session.commit()

    print("Banco de dados inicializado e populado com sucesso!")
    session.close()


if __name__ == '__main__':
    main()
