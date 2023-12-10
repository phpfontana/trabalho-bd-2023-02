-- Deleta o banco de dados, se ele existir
SELECT 'DROP DATABASE bd_2023_02' WHERE EXISTS (SELECT FROM pg_database WHERE datname = 'bd_2023_02')\gexec

SELECT 'CREATE DATABASE bd_2023_02' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'bd_2023_02')\gexec

-- Conecta no banco de dados aula
\c bd_2023_02;

-- Table "Autores"
CREATE TABLE IF NOT EXISTS Autores (
  id_autor SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cpf CHAR(11) UNIQUE NOT NULL,
  nacionalidade VARCHAR(50) NOT NULL
);

-- Table "Livros"
CREATE TABLE IF NOT EXISTS Livros (
  idLivros SERIAL PRIMARY KEY,
  titulo VARCHAR(45) NOT NULL,
  ISBN VARCHAR(45) UNIQUE NOT NULL,
  ano INT NOT NULL CHECK (ano > 0),
  editora VARCHAR(45) NOT NULL,
  quantidade INT NOT NULL CHECK (quantidade >= 0),
  Categoria VARCHAR(45) NOT NULL
);

-- Table "Usuarios"
CREATE TABLE IF NOT EXISTS Usuarios (
  idUsuarios SERIAL PRIMARY KEY,
  nickname VARCHAR(45) UNIQUE NOT NULL,
  senha VARCHAR(45) NOT NULL,
  matricula VARCHAR(45) UNIQUE NOT NULL,
  permissao VARCHAR(45) NOT NULL
);

-- Table "Emprestimos"
CREATE TABLE IF NOT EXISTS Emprestimos (
  idEmprestimos SERIAL PRIMARY KEY,
  status_emprestimo VARCHAR(45) NOT NULL,
  data_emprestimo DATE NOT NULL,
  data_devolucao DATE NOT NULL,
  Usuarios_idUsuarios INT NOT NULL REFERENCES Usuarios(idUsuarios),
  Livros_idLivros INT NOT NULL REFERENCES Livros(idLivros)
);

-- Table "Reservas"
CREATE TABLE IF NOT EXISTS Reservas (
  idReservas SERIAL PRIMARY KEY,
  status_reserva VARCHAR(45) NOT NULL,
  data_reserva DATE NOT NULL,
  Livros_idLivros INT NOT NULL REFERENCES Livros(idLivros),
  Usuarios_idUsuarios INT NOT NULL REFERENCES Usuarios(idUsuarios)
);

-- Table "Autores_dos_Livros" (Many-to-Many relationship between Autores and Livros)
CREATE TABLE IF NOT EXISTS Autores_dos_Livros (
  Autores_id_autor INT NOT NULL REFERENCES Autores(id_autor),
  Livros_idLivros INT NOT NULL REFERENCES Livros(idLivros),
  PRIMARY KEY (Autores_id_autor, Livros_idLivros)
);

-- Table "Curso"
CREATE TABLE IF NOT EXISTS Curso (
  idCurso SERIAL PRIMARY KEY,
  Descricao VARCHAR(45) NOT NULL
);

-- Table "Professor"
CREATE TABLE IF NOT EXISTS Professor (
  idProfessor SERIAL PRIMARY KEY,
  data_contratacao DATE NOT NULL,
  regime_trabalho VARCHAR(45) NOT NULL,
  Curso_idCurso INT NOT NULL REFERENCES Curso(idCurso),
  Usuarios_idUsuarios INT NOT NULL REFERENCES Usuarios(idUsuarios)
);

-- Table "Aluno"
CREATE TABLE IF NOT EXISTS Aluno (
  idAluno SERIAL PRIMARY KEY,
  data_ingresso DATE NOT NULL,
  data_previsao_conclusao DATE NOT NULL,
  Curso_idCurso INT NOT NULL REFERENCES Curso(idCurso),
  Usuarios_idUsuarios INT NOT NULL REFERENCES Usuarios(idUsuarios)
);

-- Table "Funcionario"
CREATE TABLE IF NOT EXISTS Funcionario (
  idFuncionario SERIAL PRIMARY KEY,
  data_contratacao DATE NOT NULL,
  Usuarios_idUsuarios INT NOT NULL REFERENCES Usuarios(idUsuarios)
);

-- Alteração na tabela Emprestimos para adicionar CASCADE DELETE
ALTER TABLE Emprestimos
DROP CONSTRAINT IF EXISTS emprestimos_usuarios_fk,
ADD CONSTRAINT emprestimos_usuarios_fk
    FOREIGN KEY (Usuarios_idUsuarios)
    REFERENCES Usuarios(idUsuarios)
    ON DELETE CASCADE;

-- Alteração na tabela Reservas para adicionar CASCADE DELETE
ALTER TABLE Reservas
DROP CONSTRAINT IF EXISTS reservas_usuarios_fk,
ADD CONSTRAINT reservas_usuarios_fk
    FOREIGN KEY (Usuarios_idUsuarios)
    REFERENCES Usuarios(idUsuarios)
    ON DELETE CASCADE;

-- Alteração na tabela Professor para adicionar CASCADE DELETE
ALTER TABLE Professor
DROP CONSTRAINT IF EXISTS professor_usuarios_fk,
ADD CONSTRAINT professor_usuarios_fk
    FOREIGN KEY (Usuarios_idUsuarios)
    REFERENCES Usuarios(idUsuarios)
    ON DELETE CASCADE;

-- Alteração na tabela Aluno para adicionar CASCADE DELETE
ALTER TABLE Aluno
DROP CONSTRAINT IF EXISTS aluno_usuarios_fk,
ADD CONSTRAINT aluno_usuarios_fk
    FOREIGN KEY (Usuarios_idUsuarios)
    REFERENCES Usuarios(idUsuarios)
    ON DELETE CASCADE;

-- Alteração na tabela Funcionario para adicionar CASCADE DELETE
ALTER TABLE Funcionario
DROP CONSTRAINT IF EXISTS funcionario_usuarios_fk,
ADD CONSTRAINT funcionario_usuarios_fk
    FOREIGN KEY (Usuarios_idUsuarios)
    REFERENCES Usuarios(idUsuarios)
    ON DELETE CASCADE;

