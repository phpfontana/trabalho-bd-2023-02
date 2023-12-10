from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, NoResultFound

from app.model.models import Usuario, Funcionario

# Configuração do engine e sessão do SQLAlchemy (deve ser configurada com suas credenciais)
engine = create_engine('postgresql://usuario:senha@localhost/bd_2023_02')
Session = sessionmaker(bind=engine)


class FuncionarioController:

    @staticmethod
    def criar_funcionario(nickname, senha, matricula, permissao, data_contratacao):
        """ Cria um novo usuário e funcionário no banco de dados. """
        session = Session()

        try:
            # Cria um novo objeto Usuario
            novo_usuario = Usuario(
                nickname=nickname,
                senha=senha,  # Idealmente, você deve usar um hash de senha aqui!
                matricula=matricula,
                permissao=permissao
            )
            session.add(novo_usuario)
            session.flush()  # Isso irá atribuir um ID ao novo usuário

            # Cria um novo objeto Funcionario associado ao usuário
            novo_funcionario = Funcionario(
                data_contratacao=data_contratacao,
                Usuarios_idUsuarios=novo_usuario.idUsuarios
            )
            session.add(novo_funcionario)

            # Commita a transação
            session.commit()
            return novo_funcionario
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_funcionario(id_funcionario):
        """ Busca um funcionário pelo ID. """
        session = Session()
        try:
            funcionario = session.query(Funcionario).filter_by(idFuncionario=id_funcionario).one()
            return funcionario
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_funcionario(id_funcionario, **kwargs):
        """ Atualiza os dados de um funcionário. """
        session = Session()
        try:
            funcionario = session.query(Funcionario).filter_by(idFuncionario=id_funcionario).one()
            for key, value in kwargs.items():
                setattr(funcionario, key, value)
            session.commit()
            return funcionario
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_funcionario(id_funcionario):
        """ Exclui um funcionário do banco de dados. """
        session = Session()
        try:
            funcionario = session.query(Funcionario).filter_by(idFuncionario=id_funcionario).one()
            session.delete(funcionario)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

# Exemplo de como os métodos seriam chamados: novo_funcionario = FuncionarioController.criar_funcionario('nickname',
# 'senha', 'matricula', 'permissao', '2023-01-01') funcionario = FuncionarioController.buscar_funcionario(1)
# atualizado = FuncionarioController.atualizar_funcionario(1, nickname='novo_nickname')
# FuncionarioController.deletar_funcionario(1)

# Aqui você pode adicionar mais métodos conforme necessário, como
# editar_funcionario, deletar_funcionario, buscar_funcionario, etc.
