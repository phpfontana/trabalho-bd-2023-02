from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Autor(Base):
    __tablename__ = 'Autores'
    __table_args__ = {'schema': 'Biblioteca'}

    id_autor = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    nacionalidade = Column(String(50), nullable=False)

    # Relacionamento com a tabela Autores_dos_Livros
    livros = relationship("Livro", secondary="Biblioteca.Autores_dos_Livros")


class Livro(Base):
    __tablename__ = 'Livros'
    __table_args__ = {'schema': 'Biblioteca'}

    idLivros = Column(Integer, primary_key=True)
    titulo = Column(String(45), nullable=False)
    ISBN = Column(String(45), unique=True, nullable=False)
    ano = Column(Integer, nullable=False)
    editora = Column(String(45), nullable=False)
    quantidade = Column(Integer, nullable=False)
    Categoria = Column(String(45), nullable=False)

    # Relacionamento com a tabela Autores_dos_Livros
    autores = relationship("Autor", secondary="Biblioteca.Autores_dos_Livros")


class Usuario(Base):
    __tablename__ = 'Usuarios'
    __table_args__ = {'schema': 'Biblioteca'}

    idUsuarios = Column(Integer, primary_key=True)
    nickname = Column(String(45), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)
    matricula = Column(String(45), unique=True, nullable=False)
    permissao = Column(String(45), nullable=False)
    autenticados = Column(Boolean, nullable=False)


class Emprestimo(Base):
    __tablename__ = 'Emprestimos'
    __table_args__ = {'schema': 'Biblioteca'}

    idEmprestimos = Column(Integer, primary_key=True)
    status_emprestimo = Column(String(45), nullable=False)
    data_emprestimo = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=False)
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Biblioteca.Usuarios.idUsuarios'))
    Livros_idLivros = Column(Integer, ForeignKey('Biblioteca.Livros.idLivros'))


class Reserva(Base):
    __tablename__ = 'Reservas'
    __table_args__ = {'schema': 'Biblioteca'}

    idReservas = Column(Integer, primary_key=True)
    status_reserva = Column(String(45), nullable=False)
    data_reserva = Column(Date, nullable=False)
    Livros_idLivros = Column(Integer, ForeignKey('Biblioteca.Livros.idLivros'))
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Biblioteca.Usuarios.idUsuarios'))


class AutoresDosLivros(Base):
    __tablename__ = 'Autores_dos_Livros'
    __table_args__ = {'schema': 'Biblioteca'}

    Autores_id_autor = Column(Integer, ForeignKey('Biblioteca.Autores.id_autor'), primary_key=True)
    Livros_idLivros = Column(Integer, ForeignKey('Biblioteca.Livros.idLivros'), primary_key=True)


class Curso(Base):
    __tablename__ = 'Curso'
    __table_args__ = {'schema': 'Biblioteca'}

    idCurso = Column(Integer, primary_key=True)
    Descricao = Column(String(45), nullable=False)


class Professor(Base):
    __tablename__ = 'Professor'
    __table_args__ = {'schema': 'Biblioteca'}

    idProfessor = Column(Integer, primary_key=True)
    data_contratacao = Column(Date, nullable=False)
    regime_trabalho = Column(String(45), nullable=False)
    Curso_idCurso = Column(Integer, ForeignKey('Biblioteca.Curso.idCurso'))
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Biblioteca.Usuarios.idUsuarios'))


class Aluno(Base):
    __tablename__ = 'Aluno'
    __table_args__ = {'schema': 'Biblioteca'}

    idAluno = Column(Integer, primary_key=True)
    data_ingresso = Column(Date, nullable=False)
    data_previsao_conclusao = Column(Date, nullable=False)
    Curso_idCurso = Column(Integer, ForeignKey('Biblioteca.Curso.idCurso'))
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Biblioteca.Usuarios.idUsuarios'))


class Funcionario(Base):
    __tablename__ = 'Funcionario'
    __table_args__ = {'schema': 'Biblioteca'}

    idFuncionario = Column(Integer, primary_key=True)
    data_contratacao = Column(Date, nullable=False)
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Biblioteca.Usuarios.idUsuarios'))
