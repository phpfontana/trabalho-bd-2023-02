from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

from app.utils.utils import get_engine_from_config


Base = declarative_base()


class Autor(Base):
    __tablename__ = 'Autores'

    id_autor = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    nacionalidade = Column(String(50), nullable=False)
    livros = relationship("Livro", secondary="Autores_dos_Livros", overlaps="autores")


class Livro(Base):
    __tablename__ = 'Livros'

    idLivros = Column(Integer, primary_key=True)
    titulo = Column(String(45), nullable=False)
    ISBN = Column(String(45), unique=True, nullable=False)
    ano = Column(Integer, nullable=False)
    editora = Column(String(45), nullable=False)
    quantidade = Column(Integer, nullable=False)
    Categoria = Column(String(45), nullable=False)
    autores = relationship("Autor", secondary="Autores_dos_Livros", overlaps="livros")


class Usuario(Base):
    __tablename__ = 'Usuarios'

    idUsuarios = Column(Integer, primary_key=True)
    nickname = Column(String(45), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)
    matricula = Column(String(45), unique=True, nullable=False)
    permissao = Column(String(45), nullable=False)
    # Adicionando relações
    professor = relationship("Professor", back_populates="usuario", uselist=False, cascade="all, delete-orphan")
    aluno = relationship("Aluno", back_populates="usuario", uselist=False, cascade="all, delete-orphan")
    funcionario = relationship("Funcionario", back_populates="usuario", uselist=False, cascade="all, delete-orphan")



class Emprestimo(Base):
    __tablename__ = 'Emprestimos'

    idEmprestimos = Column(Integer, primary_key=True)
    status_emprestimo = Column(String(45), nullable=False)
    data_emprestimo = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=False)
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Usuarios.idUsuarios'))
    Livros_idLivros = Column(Integer, ForeignKey('Livros.idLivros'))


class Reserva(Base):
    __tablename__ = 'Reservas'

    idReservas = Column(Integer, primary_key=True)
    status_reserva = Column(String(45), nullable=False)
    data_reserva = Column(Date, nullable=False)
    Livros_idLivros = Column(Integer, ForeignKey('Livros.idLivros'))
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Usuarios.idUsuarios'))


class AutoresDosLivros(Base):
    __tablename__ = 'Autores_dos_Livros'

    Autores_id_autor = Column(Integer, ForeignKey('Autores.id_autor'), primary_key=True)
    Livros_idLivros = Column(Integer, ForeignKey('Livros.idLivros'), primary_key=True)


class Curso(Base):
    __tablename__ = 'Curso'

    idCurso = Column(Integer, primary_key=True)
    Descricao = Column(String(45), nullable=False)


class Professor(Base):
    __tablename__ = 'Professor'

    idProfessor = Column(Integer, primary_key=True)
    data_contratacao = Column(Date, nullable=False)
    regime_trabalho = Column(String(45), nullable=False)
    Curso_idCurso = Column(Integer, ForeignKey('Curso.idCurso'))
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Usuarios.idUsuarios'))
    usuario = relationship("Usuario", back_populates="professor")

class Aluno(Base):
    __tablename__ = 'Aluno'

    idAluno = Column(Integer, primary_key=True)
    data_ingresso = Column(Date, nullable=False)
    data_previsao_conclusao = Column(Date, nullable=False)
    Curso_idCurso = Column(Integer, ForeignKey('Curso.idCurso'))
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Usuarios.idUsuarios'))
    usuario = relationship("Usuario", back_populates="aluno")


class Funcionario(Base):
    __tablename__ = 'Funcionario'

    idFuncionario = Column(Integer, primary_key=True)
    data_contratacao = Column(Date, nullable=False)
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Usuarios.idUsuarios'))
    usuario = relationship("Usuario", back_populates="funcionario")


def create_all():
    engine = get_engine_from_config()
    Base.metadata.create_all(engine)
