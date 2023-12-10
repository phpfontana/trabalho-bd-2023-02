from sqlalchemy.exc import NoResultFound, IntegrityError

from app.model.models import Usuario
from app.utils.utils import get_session


class UsuarioController:

    @staticmethod
    def criar_usuario(nickname, senha, matricula, permissao):
        """ Cria um novo usuário. """
        session = get_session()

        try:
            novo_usuario = Usuario(
                nickname=nickname,
                senha=senha,
                matricula=matricula,
                permissao=permissao
            )
            session.add(novo_usuario)
            session.commit()
            return novo_usuario
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_usuario(id_usuario):
        """ Busca um usuário pelo ID. """
        session = get_session()
        try:
            usuario = session.query(Usuario).filter_by(idUsuarios=id_usuario).one()
            return usuario
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def buscar_usuario_por_nome(nickname):
        """ Busca um usuário pelo nome. """
        session = get_session()
        try:
            usuario = session.query(Usuario).filter_by(nickname=nickname).one()
            return usuario
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_usuario(id_usuario, **kwargs):
        """ Atualiza os dados de um usuário. """
        session = get_session()
        try:
            usuario = session.query(Usuario).filter_by(idUsuarios=id_usuario).one()
            for key, value in kwargs.items():
                setattr(usuario, key, value)
            session.commit()
            return usuario
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_usuario(id_usuario):
        """ Exclui um usuário do banco de dados. """
        session = get_session()
        try:
            usuario = session.query(Usuario).filter_by(idUsuarios=id_usuario).one()
            session.delete(usuario)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def buscar_usuarios():
        """ Busca todos os usuários. """
        session = get_session()
        try:
            usuarios = session.query(Usuario).all()
            return usuarios
        finally:
            session.close()


# Exemplo de uso dos métodos:
# novo_usuario = UsuarioController.criar_usuario('nickname', 'senha', 'matricula', 'permissao')
# usuario = UsuarioController.buscar_usuario(1)
# usuario_nome = UsuarioController.buscar_usuario_por_nome('nickname')
# atualizado = UsuarioController.atualizar_usuario(1, nickname='novo_nickname')
# UsuarioController.deletar_usuario(1)


def main():
    usuarios = UsuarioController.buscar_usuarios()

    for usuario in usuarios:
        print(f"ID: {usuario.idUsuarios} - Nome: {usuario.nickname} - Matricula: {usuario.matricula} - Permissao: {usuario.permissao}")


if __name__ == '__main__':
    main()
