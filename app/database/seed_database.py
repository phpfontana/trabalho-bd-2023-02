from app.model.models import Autor, Livro, Usuario, AutoresDosLivros
from app.utils.utils import get_session


def main():
    session = get_session()

    try:
        # Insira autores
        autores = [
            Autor(nome='Machado de Assis', cpf='11122233344', nacionalidade='Brasileira'),
            Autor(nome='Clarice Lispector', cpf='22233344455', nacionalidade='Brasileira'),
            # Adicione os demais autores
        ]

        session.add_all(autores)

        # Insira livros
        livros = [
            Livro(titulo='Dom Casmurro', ISBN='ISBN12345', ano=1899, editora='Editora A', quantidade=5,
                  Categoria='Romance'),
            Livro(titulo='A Hora da Estrela', ISBN='ISBN23456', ano=1977, editora='Editora B', quantidade=3,
                  Categoria='Romance'),
            # Adicione os demais livros
        ]

        session.add_all(livros)

        # Insira usuário
        usuario = Usuario(nickname='admin', senha='123456', matricula='123456', permissao='admin')
        session.add(usuario)

        # Commit as alterações
        session.commit()

        # Associações de autores com livros
        associacoes = [
            AutoresDosLivros(Autores_id_autor=1, Livros_idLivros=1),
            AutoresDosLivros(Autores_id_autor=2, Livros_idLivros=2),
            # Adicione as demais associações
        ]

        session.add_all(associacoes)

        # Commit as alterações
        session.commit()

    except Exception:
        raise
    finally:
        session.close()


if __name__ == '__main__':
    main()
