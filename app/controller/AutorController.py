from sqlalchemy.exc import IntegrityError, NoResultFound

from app.model.models import Autor, Livro, AutoresDosLivros
from app.utils.utils import get_session


class AutoresController:

    @staticmethod
    def criar_autor(nome, cpf, nacionalidade):
        """ Cria um novo autor. """
        session = get_session()

        try:
            # Cria um novo objeto Autor
            novo_autor = Autor(
                nome=nome,
                cpf=cpf,
                nacionalidade=nacionalidade
            )
            session.add(novo_autor)
            session.commit()
            return novo_autor
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    # Métodos para buscar, atualizar e deletar autores podem ser adicionados aqui.

    @staticmethod
    def buscar_livro(id_livro):
        """ Busca um livro pelo ID. """
        session = get_session()
        try:
            livro = session.query(Livro).filter_by(idLivros=id_livro).one()
            return livro
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_livro(id_livro, **kwargs):
        """ Atualiza os dados de um livro. """
        session = get_session()
        try:
            livro = session.query(Livro).filter_by(idLivros=id_livro).one()
            for key, value in kwargs.items():
                setattr(livro, key, value)
            session.commit()
            return livro
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_livro(id_livro):
        """ Exclui um livro do banco de dados. """
        session = get_session()
        try:
            livro = session.query(Livro).filter_by(idLivros=id_livro).one()
            session.delete(livro)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()
    @staticmethod
    def buscar_autor(id_autor):
        """ Busca um autor pelo ID. """
        session = get_session()
        try:
            autor = session.query(Autor).filter_by(id_autor=id_autor).one()
            return autor
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_autor(id_autor, **kwargs):
        """ Atualiza os dados de um autor. """
        session = get_session()
        try:
            autor = session.query(Autor).filter_by(id_autor=id_autor).one()
            for key, value in kwargs.items():
                setattr(autor, key, value)
            session.commit()
            return autor
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_autor(id_autor):
        """ Exclui um autor e suas associações na tabela Autores_dos_Livros do banco de dados. """
        session = get_session()
        try:
            # Primeiro, exclui todas as entradas de associação na tabela Autores_dos_Livros
            session.query(AutoresDosLivros).filter_by(Autores_id_autor=id_autor).delete()

            # Em seguida, exclui o autor
            autor = session.query(Autor).filter_by(id_autor=id_autor).one()
            session.delete(autor)

            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()



# Exemplo de uso dos métodos:
# novo_autor = AutoresController.criar_autor('Nome do Autor', '12345678901', 'Nacionalidade')
# autor = AutoresController.buscar_autor(1)
# atualizado = AutoresController.atualizar_autor(1, nome='Novo Nome')
# AutoresController.deletar_autor(1)