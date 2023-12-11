from sqlalchemy.orm import joinedload
from app.model.models import Aluno, Usuario, Curso
from app.utils.utils import get_session
from sqlalchemy.exc import NoResultFound, IntegrityError


class AlunoController:

    @staticmethod
    def criar_aluno(nickname, senha, matricula, permissao, data_ingresso, data_previsao_conclusao, curso_descricao):
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

            aluno = Aluno(
                data_ingresso=data_ingresso,
                data_previsao_conclusao=data_previsao_conclusao,
                Curso_idCurso=curso.idCurso,
                Usuarios_idUsuarios=usuario.idUsuarios
            )
            session.add(aluno)
            session.commit()
            return aluno
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def buscar_aluno_por_nome(nickname):
        session = get_session()
        try:
            aluno = session.query(Aluno). \
                join(Usuario). \
                filter(Usuario.nickname == nickname). \
                options(joinedload(Aluno.usuario), joinedload(Aluno.curso)). \
                one()
            return aluno
        except NoResultFound:
            return None
        finally:
            session.close()


    @staticmethod
    def buscar_aluno_por_usuario_id(usuario_id):
        """ Busca um aluno pelo ID do usuário associado. """
        session = get_session()
        try:
            aluno = session.query(Aluno).filter_by(Usuarios_idUsuarios=usuario_id).one()
            return aluno
        except NoResultFound:
            return None
        finally:
            session.close()


    @staticmethod
    def atualizar_aluno(id_aluno, **kwargs):
        session = get_session()
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

    def atualizar_aluno_usuario(aluno_id, **kwargs):
        session = get_session()
        try:
            aluno = session.query(Aluno).filter_by(idAluno=aluno_id).one()

            # Atributos específicos do Aluno
            aluno_attrs = ['data_ingresso', 'data_previsao_conclusao',
                           'Curso_idCurso']  # Adicione outros atributos de Aluno aqui
            usuario_attrs = ['nickname', 'senha', 'matricula', 'permissao']  # Adicione outros atributos de Usuario aqui

            # Atualiza atributos do Aluno
            for key, value in kwargs.items():
                if key in aluno_attrs:
                    setattr(aluno, key, value)

            # Atualiza atributos do Usuario associado
            usuario = aluno.usuario
            for key, value in kwargs.items():
                if key in usuario_attrs:
                    setattr(usuario, key, value)

            session.commit()
            return aluno
        except NoResultFound:
            session.rollback()
            return None
        finally:
            session.close()

    @staticmethod
    def deletar_aluno(id_aluno):
        session = get_session()
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
# novo_aluno = AlunoController.criar_aluno('nickname', 'senha', 'matricula', 'permissao', 'data_ingresso', 'data_previsao_conclusao', 'curso_descricao')
# aluno = AlunoController.buscar_aluno_por_nome('nickname')
# atualizado = AlunoController.atualizar_aluno(1, data_ingresso='nova_data_ingresso')
# AlunoController.deletar_aluno(1)
