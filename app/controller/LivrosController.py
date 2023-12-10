from sqlalchemy.exc import NoResultFound, IntegrityError
from app.utils.utils import get_session
from app.model.models import Livro


class LivroController:

    @staticmethod
    def criar_livro(titulo, ISBN, ano, editora, quantidade, Categoria):
        session = get_session()
        try:
            novo_livro = Livro(
                titulo=titulo,
                ISBN=ISBN,
                ano=ano,
                editora=editora,
                quantidade=quantidade,
                Categoria=Categoria
            )
            session.add(novo_livro)
            session.commit()
            return novo_livro
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_livro_por_id(id_livro):
        session = get_session()
        try:
            livro = session.query(Livro).filter_by(idLivros=id_livro).one()
            return livro
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def buscar_livros():
        session = get_session()
        try:
            livros = session.query(Livro).all()
            return livros
        finally:
            session.close()

    @staticmethod
    def atualizar_livro(id_livro, **kwargs):
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
        session = get_session()
        try:
            livro = session.query(Livro).filter_by(idLivros=id_livro).one()
            session.delete(livro)
            session.commit()
        except NoResultFound:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def buscar_livro_por_titulo(titulo):
        session = get_session()
        try:
            livro = session.query(Livro).filter_by(titulo=titulo).one()
            return livro
        except NoResultFound:
            return None
        finally:
            session.close()

# Exemplo de uso dos métodos:
# novo_livro = LivroController.criar_livro('Dom Casmurro', 'ISBN12345', 1899, 'Editora A', 5, 'Romance')
# livro = LivroController.buscar_livro_por_id(1)
# livros = LivroController.buscar_livros()
# atualizado = LivroController.atualizar_livro(1, titulo='Novo Título')
# LivroController.deletar_livro(1)
# livro = LivroController.buscar_livro_por_titulo('Dom Casmurro')
