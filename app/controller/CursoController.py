from sqlalchemy.exc import NoResultFound, IntegrityError
from app.utils.utils import get_session
from app.model.models import Curso


class CursoController:

    @staticmethod
    def criar_curso(descricao):
        """ Cria um novo curso. """
        session = get_session()

        try:
            # Cria um novo objeto Curso
            novo_curso = Curso(
                Descricao=descricao
            )
            session.add(novo_curso)
            session.commit()
            return novo_curso
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_curso(id_curso):
        """ Busca um curso pelo ID. """
        session = get_session()
        try:
            curso = session.query(Curso).filter_by(idCurso=id_curso).one()
            return curso
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_curso(id_curso, **kwargs):
        """ Atualiza os dados de um curso. """
        session = get_session()
        try:
            curso = session.query(Curso).filter_by(idCurso=id_curso).one()
            for key, value in kwargs.items():
                setattr(curso, key, value)
            session.commit()
            return curso
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_curso(id_curso):
        """ Exclui um curso do banco de dados. """
        session = get_session()
        try:
            curso = session.query(Curso).filter_by(idCurso=id_curso).one()
            session.delete(curso)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

# Exemplo de uso dos métodos:
# novo_curso = CursoController.criar_curso('Ciência da Computação')
# curso = CursoController.buscar_curso(1)
# atualizado = CursoController.atualizar_curso(1, Descricao='Engenharia de Software')
# CursoController.deletar_curso(1)
