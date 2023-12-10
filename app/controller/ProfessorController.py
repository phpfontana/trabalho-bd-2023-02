from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.orm import sessionmaker

from app.model.models import Professor, Usuario
# Configuração do engine e sessão do SQLAlchemy (deve ser configurada com suas credenciais)
engine = create_engine('postgresql://usuario:senha@localhost/bd_2023_02')
Session = sessionmaker(bind=engine)


class ProfessorController:

    @staticmethod
    def criar_professor(nickname, senha, matricula, permissao, data_contratacao, regime_trabalho, id_curso):
        """ Cria um novo usuário e professor no banco de dados. """
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

            # Cria um novo objeto Professor associado ao usuário
            novo_professor = Professor(
                data_contratacao=data_contratacao,
                regime_trabalho=regime_trabalho,
                Curso_idCurso=id_curso,
                Usuarios_idUsuarios=novo_usuario.idUsuarios
            )
            session.add(novo_professor)

            # Commita a transação
            session.commit()
            return novo_professor
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_professor(id_professor):
        """ Busca um professor pelo ID. """
        session = Session()
        try:
            professor = session.query(Professor).filter_by(idProfessor=id_professor).one()
            return professor
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_professor(id_professor, **kwargs):
        """ Atualiza os dados de um professor. """
        session = Session()
        try:
            professor = session.query(Professor).filter_by(idProfessor=id_professor).one()
            for key, value in kwargs.items():
                setattr(professor, key, value)
            session.commit()
            return professor
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_professor(id_professor):
        """ Exclui um professor do banco de dados. """
        session = Session()
        try:
            professor = session.query(Professor).filter_by(idProfessor=id_professor).one()
            session.delete(professor)
            session.commit()
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

# Exemplo de uso dos métodos:
# novo_professor = ProfessorController.criar_professor('nickname', 'senha', 'matricula', 'permissao', '2023-01-01', 'Integral', 1)
# professor = ProfessorController.buscar_professor(1)
# atualizado = ProfessorController.atualizar_professor(1, regime_trabalho='Parcial')
# ProfessorController.deletar_professor(1)
