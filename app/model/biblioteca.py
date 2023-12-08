from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Autor(db.Model):
    __tablename__ = 'autores'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nacionalidade = db.Column(db.String(50), nullable=False)


class Livro(db.Model):
    __tablename__ = 'livros'
    idLivros = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(45), nullable=False)
    ISBN = db.Column(db.String(45), unique=True, nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    editora = db.Column(db.String(45), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    Categoria = db.Column(db.String(45), nullable=False)


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuarios = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(45), unique=True, nullable=False)
    senha = db.Column(db.String(45), nullable=False)
    matricula = db.Column(db.String(45), unique=True, nullable=False)
    permissao = db.Column(db.String(45), nullable=False)
    autenticados = db.Column(db.Boolean, nullable=False)


class Emprestimo(db.Model):
    __tablename__ = 'emprestimos'
    idEmprestimos = db.Column(db.Integer, primary_key=True)
    status_emprestimo = db.Column(db.String(45), nullable=False)
    data_emprestimo = db.Column(db.Date, nullable=False)
    data_devolucao = db.Column(db.Date, nullable=False)
    Usuarios_idUsuarios = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuarios'), nullable=False)
    Livros_idLivros = db.Column(db.Integer, db.ForeignKey('livros.idLivros'), nullable=False)


class Reserva(db.Model):
    __tablename__ = 'reservas'
    idReservas = db.Column(db.Integer, primary_key=True)
    status_reserva = db.Column(db.String(45), nullable=False)
    data_reserva = db.Column(db.Date, nullable=False)
    Livros_idLivros = db.Column(db.Integer, db.ForeignKey('livros.idLivros'), nullable=False)
    Usuarios_idUsuarios = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuarios'), nullable=False)


class AutoresLivros(db.Model):
    __tablename__ = 'autores_dos_livros'
    Autores_id_autor = db.Column(db.Integer, db.ForeignKey('autores.id_autor'), primary_key=True)
    Livros_idLivros = db.Column(db.Integer, db.ForeignKey('livros.idLivros'), primary_key=True)


class Curso(db.Model):
    __tablename__ = 'curso'
    idCurso = db.Column(db.Integer, primary_key=True)
    Descricao = db.Column(db.String(45), nullable=False)


class Professor(db.Model):
    __tablename__ = 'professor'
    idProfessor = db.Column(db.Integer, primary_key=True)
    data_contratacao = db.Column(db.Date, nullable=False)
    regime_trabalho = db.Column(db.String(45), nullable=False)
    Curso_idCurso = db.Column(db.Integer, db.ForeignKey('curso.idCurso'), nullable=False)
    Usuarios_idUsuarios = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuarios'), nullable=False)


class Aluno(db.Model):
    __tablename__ = 'aluno'
    idAluno = db.Column(db.Integer, primary_key=True)
    data_ingresso = db.Column(db.Date, nullable=False)
    data_previsao_conclusao = db.Column(db.Date, nullable=False)
    Curso_idCurso = db.Column(db.Integer, db.ForeignKey('curso.idCurso'), nullable=False)
    Usuarios_idUsuarios = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuarios'), nullable=False)


class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    idFuncionario = db.Column(db.Integer, primary_key=True)
    data_contratacao = db.Column(db.Date, nullable=False)
    Usuarios_idUsuarios = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuarios'), nullable=False)
