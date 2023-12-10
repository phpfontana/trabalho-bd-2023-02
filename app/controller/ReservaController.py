from sqlalchemy.exc import IntegrityError, NoResultFound

from app.model.models import Reserva
from app.utils.utils import get_session


class ReservasController:

    @staticmethod
    def criar_reserva(status_reserva, data_reserva, usuario_id, livro_id):
        """ Cria uma nova reserva. """
        session = get_session()

        try:
            nova_reserva = Reserva(
                status_reserva=status_reserva,
                data_reserva=data_reserva,
                Usuarios_idUsuarios=usuario_id,
                Livros_idLivros=livro_id
            )
            session.add(nova_reserva)
            session.commit()
            return nova_reserva
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_reserva(id_reserva):
        """ Busca uma reserva pelo ID. """
        session = get_session()
        try:
            reserva = session.query(Reserva).filter_by(idReservas=id_reserva).one()
            return reserva
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_reserva(id_reserva, **kwargs):
        """ Atualiza os dados de uma reserva. """
        session = get_session()
        try:
            reserva = session.query(Reserva).filter_by(idReservas=id_reserva).one()
            for key, value in kwargs.items():
                setattr(reserva, key, value)
            session.commit()
            return reserva
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_reserva(id_reserva):
        """ Exclui uma reserva do banco de dados. """
        session = get_session()
        try:
            reserva = session.query(Reserva).filter_by(idReservas=id_reserva).one()
            session.delete(reserva)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

# Exemplo de uso dos métodos:
# nova_reserva = ReservasController.criar_reserva('pendente', '2023-01-01', 1, 1)
# reserva = ReservasController.buscar_reserva(1)
# atualizado = ReservasController.atualizar_reserva(1, status_reserva='confirmada')
# ReservasController.deletar_reserva(1)
