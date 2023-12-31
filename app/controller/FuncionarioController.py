from sqlalchemy.orm import joinedload

from app.controller.UsuarioController import UsuarioController
from app.model.models import Funcionario, Usuario
from app.utils.utils import get_session
from sqlalchemy.exc import NoResultFound, IntegrityError


class FuncionarioController:

    @staticmethod
    def criar_funcionario(nickname, senha, matricula, permissao, data_contratacao):
        session = get_session()
        try:
            usuario = Usuario(
                nickname=nickname,
                senha=senha,
                matricula=matricula,
                permissao=permissao
            )
            session.add(usuario)
            session.flush()  # Isso é necessário para obter o ID do usuário recém-criado

            funcionario = Funcionario(
                data_contratacao=data_contratacao,
                Usuarios_idUsuarios=usuario.idUsuarios
            )
            session.add(funcionario)
            session.commit()
            return funcionario
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_funcionario_por_nome(nickname):
        session = get_session()
        try:
            funcionario = session.query(Funcionario). \
                join(Usuario). \
                filter(Usuario.nickname == nickname). \
                options(joinedload(Funcionario.usuario)). \
                one()
            return funcionario
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def buscar_funcionario_por_usuario_id(usuario_id):
        """ Busca um funcionario pelo ID do usuário associado. """
        session = get_session()
        try:
            funcionario = session.query(Funcionario).filter_by(Usuarios_idUsuarios=usuario_id).one()
            return funcionario
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_funcionario(id_funcionario, **kwargs):
        session = get_session()
        try:
            funcionario = session.query(Funcionario).filter_by(idFuncionario=id_funcionario).one()

            # Atributos específicos do Funcionário
            funcionario_attrs = ['data_contratacao']  # Adicione outros atributos de Funcionario aqui
            usuario_attrs = ['nickname', 'senha', 'matricula', 'permissao']  # Adicione outros atributos de Usuario aqui

            # Atualiza atributos do Funcionário
            for key, value in kwargs.items():
                if key in funcionario_attrs:
                    setattr(funcionario, key, value)

            # Atualiza atributos do Usuario associado
            usuario = funcionario.usuario
            for key, value in kwargs.items():
                if key in usuario_attrs:
                    setattr(usuario, key, value)

            session.commit()
            return funcionario
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_funcionario(id_funcionario):
        session = get_session()
        try:
            funcionario = session.query(Funcionario).filter_by(idFuncionario=id_funcionario).one()
            session.delete(funcionario)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()


# Exemplo de uso dos métodos:
# novo_funcionario = FuncionarioController.criar_funcionario('nickname', 'senha', 'matricula', 'permissao', 'data_contratacao')
# funcionario = FuncionarioController.buscar_funcionario_por_nome('nickname')
# atualizado = FuncionarioController.atualizar_funcionario(1, data_contratacao='nova_data')
# FuncionarioController.deletar_funcionario(1)
