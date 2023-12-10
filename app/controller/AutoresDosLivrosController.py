from app.model.models import AutoresDosLivros, Autor, Livro
from app.utils.utils import get_session
from sqlalchemy.exc import IntegrityError, NoResultFound

class AutoresDosLivrosController:

    @staticmethod
    def associar_autor_livro(id_autor, id_livro):
        """ Associa um autor a um livro. """
        session = get_session()
        try:
            autor_livro = AutoresDosLivros(
                Autores_id_autor=id_autor,
                Livros_idLivros=id_livro
            )
            session.add(autor_livro)
            session.commit()
            return autor_livro
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_associacoes_por_autor(id_autor):
        """ Busca todas as associações de um autor específico. """
        session = get_session()
        try:
            associacoes = session.query(AutoresDosLivros).filter_by(Autores_id_autor=id_autor).all()
            return associacoes
        finally:
            session.close()

    @staticmethod
    def buscar_associacoes_por_livro(id_livro):
        """ Busca todas as associações de um livro específico. """
        session = get_session()
        try:
            associacoes = session.query(AutoresDosLivros).filter_by(Livros_idLivros=id_livro).all()
            return associacoes
        finally:
            session.close()

    @staticmethod
    def remover_associacao(id_autor, id_livro):
        """ Remove uma associação entre um autor e um livro. """
        session = get_session()
        try:
            associacao = session.query(AutoresDosLivros).filter_by(Autores_id_autor=id_autor, Livros_idLivros=id_livro).one()
            session.delete(associacao)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

# Exemplo de uso dos métodos:
# associacao = AutoresDosLivrosController.associar_autor_livro(1, 1)
# associacoes_autor = AutoresDosLivrosController.buscar_associacoes_por_autor(1)
# associacoes_livro = AutoresDosLivrosController.buscar_associacoes_por_livro(1)
# AutoresDosLivrosController.remover_associacao(1, 1)