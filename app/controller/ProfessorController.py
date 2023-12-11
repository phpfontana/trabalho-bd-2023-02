from sqlalchemy.orm import joinedload
from app.model.models import Professor, Usuario, Curso
from app.utils.utils import get_session
from sqlalchemy.exc import NoResultFound, IntegrityError


class ProfessorController:

    @staticmethod
    def criar_professor(nickname, senha, matricula, permissao, data_contratacao, regime_trabalho, curso_descricao):
        session = get_session()
        try:
            # Verifica se o curso já existe
            curso = session.query(Curso).filter_by(Descricao=curso_descricao).one_or_none()
            if not curso:
                curso = Curso(Descricao=curso_descricao)
                session.add(curso)
                session.flush()  # Isso é necessário para obter o ID do curso recém-criado

            usuario = Usuario(
                nickname=nickname,
                senha=senha,
                matricula=matricula,
                permissao=permissao
            )
            session.add(usuario)
            session.flush()  # Isso é necessário para obter o ID do usuário recém-criado

            professor = Professor(
                data_contratacao=data_contratacao,
                regime_trabalho=regime_trabalho,
                Curso_idCurso=curso.idCurso,
                Usuarios_idUsuarios=usuario.idUsuarios
            )
            session.add(professor)
            session.commit()
            return professor
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_professor_por_id(id_professor):
        """ Busca um professor pelo ID. """
        session = get_session()
        try:
            professor = session.query(Professor).filter_by(idProfessor=id_professor).one()
            return professor
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def buscar_professor_por_usuario_id(usuario_id):
        """ Busca um professor pelo ID do usuário associado. """
        session = get_session()
        try:
            professor = session.query(Professor).filter_by(Usuarios_idUsuarios=usuario_id).one()
            return professor
        except NoResultFound:
            return None
        finally:
            session.close()

    @staticmethod
    def atualizar_professor(id_professor, **kwargs):
        session = get_session()
        try:
            professor = session.query(Professor).filter_by(idProfessor=id_professor).one()

            # Atributos específicos do Professor
            professor_attrs = ['data_contratacao', 'regime_trabalho', 'Curso_idCurso']  # Adicione outros atributos de Professor aqui
            usuario_attrs = ['nickname', 'senha', 'matricula', 'permissao']  # Adicione outros atributos de Usuario aqui

            # Atualiza atributos do Professor
            for key, value in kwargs.items():
                if key in professor_attrs:
                    setattr(professor, key, value)

            # Atualiza atributos do Usuario associado
            usuario = professor.usuario
            for key, value in kwargs.items():
                if key in usuario_attrs:
                    setattr(usuario, key, value)

            session.commit()
            return professor
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_professor(id_professor):
        session = get_session()
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
# novo_professor = ProfessorController.criar_professor('nickname', 'senha', 'matricula', 'permissao', 'data_contratacao', 'regime_trabalho', 'curso_descricao')
# professor = ProfessorController.buscar_professor_por_nome('nickname')
# atualizado = ProfessorController.atualizar_professor(1, data_contratacao='nova_data_contratacao')
# ProfessorController.deletar_professor(1)


