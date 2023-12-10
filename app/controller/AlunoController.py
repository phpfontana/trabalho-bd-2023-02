from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, NoResultFound

from app.model.models import Usuario, Funcionario, Aluno

# Configuração do engine e sessão do SQLAlchemy (deve ser configurada com suas credenciais)
engine = create_engine('postgresql://usuario:senha@localhost/bd_2023_02')
Session = sessionmaker(bind=engine)


class AlunoController:

    @staticmethod
    def criar_aluno(nickname, senha, matricula, permissao, data_ingresso, data_previsao_conclusao, id_curso):
        """ Cria um novo usuário e aluno no banco de dados. """
        session = Session()

        try:
            # Cria um novo objeto Usuario
            novo_usuario = Usuario(
                nickname=nickname,
                senha=senha,  # A senha deve ser armazenada como hash.
                matricula=matricula,
                permissao=permissao
            )
            session.add(novo_usuario)
            session.flush()  # Obtém o ID do novo usuário

            # Cria um novo objeto Aluno associado ao usuário
            novo_aluno = Aluno(
                data_ingresso=data_ingresso,
                data_previsao_conclusao=data_previsao_conclusao,
                Curso_idCurso=id_curso,
                Usuarios_idUsuarios=novo_usuario.idUsuarios
            )
            session.add(novo_aluno)

            # Commita a transação
            session.commit()
            return novo_aluno
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_aluno(id_aluno):
        """ Busca um aluno pelo ID. """
        session = Session()
        try:
            aluno = session.query(Aluno).filter_by(idAluno=id_aluno).one()
            return aluno
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_aluno(id_aluno, **kwargs):
        """ Atualiza os dados de um aluno. """
        session = Session()
        try:
            aluno = session.query(Aluno).filter_by(idAluno=id_aluno).one()
            for key, value in kwargs.items():
                setattr(aluno, key, value)
            session.commit()
            return aluno
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_aluno(id_aluno):
        """ Exclui um aluno do banco de dados. """
        session = Session()
        try:
            aluno = session.query(Aluno).filter_by(idAluno=id_aluno).one()
            session.delete(aluno)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

# Exemplo de uso dos métodos:
# novo_aluno = AlunoController.criar_aluno('nickname', 'senha', 'matricula', 'permissao', '2023-01-01', '2024-01-01', 1)
# aluno = AlunoController.buscar_aluno(1)
# atualizado = AlunoController.atualizar_aluno(1, nickname='novo_nickname')
# AlunoController.deletar_aluno(1)
