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
    def buscar_professor_por_nome(nickname):
        session = get_session()
        try:
            professor = session.query(Professor). \
                join(Usuario). \
                filter(Usuario.nickname == nickname). \
                options(joinedload(Professor.usuario), joinedload(Professor.curso)). \
                one()
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

def main():
    novo_professor = ProfessorController.criar_professor('nickname', 'senha', 'matricula', 'permissao', 'data_contratacao', 'regime_trabalho', 'curso_descricao')
    professor = ProfessorController.buscar_professor_por_nome('nickname')

    # extrair id do professor
    id_professor = professor.idProfessor



if __name__ == '__main__':
    main()
