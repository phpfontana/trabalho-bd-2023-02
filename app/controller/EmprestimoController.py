from sqlalchemy.exc import NoResultFound, IntegrityError

from app.model.models import Emprestimo
from app.utils.utils import get_session


class EmprestimosController:

    @staticmethod
    def criar_emprestimo(status_emprestimo, data_emprestimo, data_devolucao, usuario_id, livro_id):
        """ Cria um novo empréstimo. """
        session = get_session()

        try:
            novo_emprestimo = Emprestimo(
                status_emprestimo=status_emprestimo,
                data_emprestimo=data_emprestimo,
                data_devolucao=data_devolucao,
                Usuarios_idUsuarios=usuario_id,
                Livros_idLivros=livro_id
            )
            session.add(novo_emprestimo)
            session.commit()
            return novo_emprestimo
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_emprestimo(id_emprestimo):
        """ Busca um empréstimo pelo ID. """
        session = get_session()
        try:
            emprestimo = session.query(Emprestimo).filter_by(idEmprestimos=id_emprestimo).one()
            return emprestimo
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_emprestimo(id_emprestimo, **kwargs):
        """ Atualiza os dados de um empréstimo. """
        session = get_session()
        try:
            emprestimo = session.query(Emprestimo).filter_by(idEmprestimos=id_emprestimo).one()
            for key, value in kwargs.items():
                setattr(emprestimo, key, value)
            session.commit()
            return emprestimo
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_emprestimo(id_emprestimo):
        """ Exclui um empréstimo do banco de dados. """
        session = get_session()
        try:
            emprestimo = session.query(Emprestimo).filter_by(idEmprestimos=id_emprestimo).one()
            session.delete(emprestimo)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

# Exemplo de uso dos métodos:
# novo_emprestimo = EmprestimosController.criar_emprestimo('ativo', '2023-01-01', '2023-01-15', 1, 1)
# emprestimo = EmprestimosController.buscar_emprestimo(1)
# atualizado = EmprestimosController.atualizar_emprestimo(1, status_emprestimo='concluido')
# EmprestimosController.deletar_emprestimo(1)
