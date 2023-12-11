from app.model.models import Autor
from app.utils.utils import get_session
from sqlalchemy.exc import NoResultFound, IntegrityError


class AutorController:

    @staticmethod
    def criar_autor(nome, cpf, nacionalidade):
        """ Cria um novo autor. """
        session = get_session()
        try:
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

    @staticmethod
    def buscar_autor_por_nome(nome):
        """ Busca um autor pelo nome. """
        session = get_session()
        try:
            autor = session.query(Autor).filter_by(nome=nome).one()
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
        """ Exclui um autor do banco de dados. """
        session = get_session()
        try:
            autor = session.query(Autor).filter_by(id_autor=id_autor).one()
            session.delete(autor)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def buscar_autores():
        """ Busca todos os autores. """
        session = get_session()
        try:
            autores = session.query(Autor).all()
            return autores
        finally:
            session.close()

# Exemplo de uso dos métodos:
# novo_autor = AutorController.criar_autor('nome', 'cpf', 'nacionalidade')
# autor = AutorController.buscar_autor_por_nome('nome')
# atualizado = AutorController.atualizar_autor(1, nome='novo_nome')
# AutorController.deletar_autor(1)
# autores = AutorController.buscar_autores()
# for autor in autores:
#     print(autor.nome, autor.cpf, autor.nacionalidade)
