from sqlalchemy_utils import database_exists, create_database, drop_database

from app.controller.AlunoController import AlunoController
from app.controller.EmprestimoController import EmprestimosController
from app.controller.FuncionarioController import FuncionarioController
from app.controller.ProfessorController import ProfessorController
from app.model.models import Base, Autor, Livro, AutoresDosLivros
from app.utils.utils import get_engine_from_config, get_session


def criar_aluno(nickname, senha, matricula, permissao, data_ingresso, data_previsao_conclusao, curso_descricao):
    AlunoController.criar_aluno(nickname, senha, matricula, permissao, data_ingresso, data_previsao_conclusao,
                                curso_descricao)


def criar_professor(nickname, senha, matricula, permissao, data_contratacao, regime_trabalho, curso_descricao):
    ProfessorController.criar_professor(nickname, senha, matricula, permissao, data_contratacao, regime_trabalho,
                                        curso_descricao)


def criar_funcionario(nickname, senha, matricula, permissao, data_contratacao):
    FuncionarioController.criar_funcionario(nickname, senha, matricula, permissao, data_contratacao)


def criar_emprestimo(status_emprestimo, data_emprestimo, data_devolucao, usuario_id, livro_id):
    EmprestimosController.criar_emprestimo(status_emprestimo, data_emprestimo, data_devolucao, usuario_id, livro_id)


def reset_database():
    engine = get_engine_from_config()

    # Exclui o banco de dados se ele já existir
    if database_exists(engine.url):
        print(f"Excluindo o banco de dados existente: {engine.url}")
        drop_database(engine.url)

    # Cria o banco de dados
    print(f"Criando o banco de dados: {engine.url}")
    create_database(engine.url)

    # Cria todas as tabelas definidas nos modelos
    Base.metadata.create_all(engine)


def main():
    reset_database()

    session = get_session()

    # Insira autores
    autores = [
        Autor(nome='Machado de Assis', cpf='11122233344', nacionalidade='Brasileira'),
        Autor(nome='Clarice Lispector', cpf='22233344455', nacionalidade='Brasileira'),
        Autor(nome='Jorge Amado', cpf='33344455566', nacionalidade='Brasileira'),
        Autor(nome='Carlos Drummond de Andrade', cpf='44455566677', nacionalidade='Brasileira'),
        Autor(nome='Cecília Meireles', cpf='55566677788', nacionalidade='Brasileira'),
        Autor(nome='João Guimarães Rosa', cpf='66677788899', nacionalidade='Brasileira'),
        Autor(nome='Lygia Fagundes Telles', cpf='77788899900', nacionalidade='Brasileira'),
        Autor(nome='Manuel Bandeira', cpf='88899900011', nacionalidade='Brasileira'),
        Autor(nome='Rachel de Queiroz', cpf='99900011122', nacionalidade='Brasileira'),
        Autor(nome='Érico Veríssimo', cpf='00011122233', nacionalidade='Brasileira')
    ]

    # Insira livros
    livros = [
        Livro(titulo='Dom Casmurro', ISBN='ISBN12345', ano=1899, editora='Editora A', quantidade=5,
              Categoria='Romance'),
        Livro(titulo='A Hora da Estrela', ISBN='ISBN23456', ano=1977, editora='Editora B', quantidade=3,
              Categoria='Romance'),
        Livro(titulo='Gabriela, Cravo e Canela', ISBN='ISBN34567', ano=1958, editora='Editora C', quantidade=4,
              Categoria='Romance'),
        Livro(titulo='Alguma Poesia', ISBN='ISBN45678', ano=1930, editora='Editora D', quantidade=6,
              Categoria='Poesia'),
        Livro(titulo='Romanceiro da Inconfidência', ISBN='ISBN56789', ano=1953, editora='Editora E', quantidade=2,
              Categoria='Poesia'),
        Livro(titulo='Grande Sertão: Veredas', ISBN='ISBN67890', ano=1956, editora='Editora F', quantidade=3,
              Categoria='Romance'),
        Livro(titulo='As Meninas', ISBN='ISBN78901', ano=1973, editora='Editora G', quantidade=5, Categoria='Romance'),
        Livro(titulo='Estrela da Vida Inteira', ISBN='ISBN89012', ano=1966, editora='Editora H', quantidade=4,
              Categoria='Poesia'),
        Livro(titulo='O Quinze', ISBN='ISBN90123', ano=1930, editora='Editora I', quantidade=2, Categoria='Romance'),
        Livro(titulo='O Tempo e o Vento', ISBN='ISBN01234', ano=1949, editora='Editora J', quantidade=3,
              Categoria='Romance'),
        Livro(titulo='Memórias Póstumas de Brás Cubas', ISBN='ISBN11111', ano=1881, editora='Editora K', quantidade=4,
              Categoria='Romance'),
        Livro(titulo='Quase Memória', ISBN='ISBN22222', ano=1995, editora='Editora L', quantidade=2,
              Categoria='Romance'),
        Livro(titulo='A Paixão Segundo GH', ISBN='ISBN33333', ano=1964, editora='Editora M', quantidade=3,
              Categoria='Romance'),
        Livro(titulo='Mar Morto', ISBN='ISBN44444', ano=1936, editora='Editora N', quantidade=5, Categoria='Romance'),
        Livro(titulo='Sentimento do Mundo', ISBN='ISBN55555', ano=1940, editora='Editora O', quantidade=6,
              Categoria='Poesia'),
        Livro(titulo='Jardim Noturno', ISBN='ISBN66666', ano=1950, editora='Editora P', quantidade=2,
              Categoria='Poesia'),
        Livro(titulo='Sagarana', ISBN='ISBN77777', ano=1946, editora='Editora Q', quantidade=3, Categoria='Conto'),
        Livro(titulo='Ciranda de Pedra', ISBN='ISBN88888', ano=1954, editora='Editora R', quantidade=4,
              Categoria='Romance'),
        Livro(titulo='Libertinagem', ISBN='ISBN99999', ano=1930, editora='Editora S', quantidade=5, Categoria='Poesia'),
        Livro(titulo='Dona Flor e Seus Dois Maridos', ISBN='ISBN12321', ano=1966, editora='Editora T', quantidade=4,
              Categoria='Romance'),
        Livro(titulo='O Alienista', ISBN='ISBN32123', ano=1882, editora='Editora U', quantidade=3, Categoria='Conto'),
        Livro(titulo='A Cidade e as Serras', ISBN='ISBN43234', ano=1901, editora='Editora V', quantidade=2,
              Categoria='Romance'),
        Livro(titulo='Vidas Secas', ISBN='ISBN54345', ano=1938, editora='Editora W', quantidade=4, Categoria='Romance'),
        Livro(titulo='Capitães da Areia', ISBN='ISBN65456', ano=1937, editora='Editora X', quantidade=5,
              Categoria='Romance'),
        Livro(titulo='Claro Enigma', ISBN='ISBN76567', ano=1951, editora='Editora Y', quantidade=3, Categoria='Poesia'),
        Livro(titulo='A Rosa do Povo', ISBN='ISBN87678', ano=1945, editora='Editora Z', quantidade=2,
              Categoria='Poesia'),
    ]

    session.add_all(autores)
    print("Autores inseridos com sucesso!")

    session.add_all(livros)
    print("Livros inseridos com sucesso!")

    session.commit()

    # Associações de autores com livros
    associacoes = [
        AutoresDosLivros(Autores_id_autor=1, Livros_idLivros=1),  # Machado de Assis - Dom Casmurro
        AutoresDosLivros(Autores_id_autor=2, Livros_idLivros=2),  # Clarice Lispector - A Hora da Estrela
        AutoresDosLivros(Autores_id_autor=3, Livros_idLivros=3),  # Jorge Amado - Gabriela, Cravo e Canela
        AutoresDosLivros(Autores_id_autor=4, Livros_idLivros=4),  # Carlos Drummond de Andrade - Alguma Poesia
        AutoresDosLivros(Autores_id_autor=5, Livros_idLivros=5),  # Cecília Meireles - Romanceiro da Inconfidência
        AutoresDosLivros(Autores_id_autor=6, Livros_idLivros=6),  # João Guimarães Rosa - Grande Sertão: Veredas
        AutoresDosLivros(Autores_id_autor=7, Livros_idLivros=7),  # Lygia Fagundes Telles - As Meninas
        AutoresDosLivros(Autores_id_autor=8, Livros_idLivros=8),  # Manuel Bandeira - Estrela da Vida Inteira
        AutoresDosLivros(Autores_id_autor=9, Livros_idLivros=9),  # Rachel de Queiroz - O Quinze
        AutoresDosLivros(Autores_id_autor=10, Livros_idLivros=10),  # Érico Veríssimo - O Tempo e o Vento
        AutoresDosLivros(Autores_id_autor=1, Livros_idLivros=11),  # Machado de Assis - Memórias Póstumas de Brás Cubas
        AutoresDosLivros(Autores_id_autor=2, Livros_idLivros=12),  # Clarice Lispector - Quase Memória
        AutoresDosLivros(Autores_id_autor=3, Livros_idLivros=13),  # Jorge Amado - Mar Morto
        AutoresDosLivros(Autores_id_autor=4, Livros_idLivros=14),  # Carlos Drummond de Andrade - Sentimento do Mundo
        AutoresDosLivros(Autores_id_autor=5, Livros_idLivros=15),  # Cecília Meireles - Jardim Noturno
        AutoresDosLivros(Autores_id_autor=6, Livros_idLivros=16),  # João Guimarães Rosa - Sagarana
        AutoresDosLivros(Autores_id_autor=7, Livros_idLivros=17),  # Lygia Fagundes Telles - Ciranda de Pedra
        AutoresDosLivros(Autores_id_autor=8, Livros_idLivros=18),  # Manuel Bandeira - Libertinagem
        AutoresDosLivros(Autores_id_autor=3, Livros_idLivros=19),  # Jorge Amado - Dona Flor e Seus Dois Maridos
        AutoresDosLivros(Autores_id_autor=1, Livros_idLivros=20),  # Machado de Assis - O Alienista
        AutoresDosLivros(Autores_id_autor=1, Livros_idLivros=21),  # Machado de Assis - A Cidade e as Serras
        AutoresDosLivros(Autores_id_autor=9, Livros_idLivros=22),  # Rachel de Queiroz - Vidas Secas
        AutoresDosLivros(Autores_id_autor=3, Livros_idLivros=23),  # Jorge Amado - Capitães da Areia
        AutoresDosLivros(Autores_id_autor=4, Livros_idLivros=24),  # Carlos Drummond de Andrade - Claro Enigma
        AutoresDosLivros(Autores_id_autor=4, Livros_idLivros=25)  # Carlos Drummond de Andrade - A Rosa do Povo
    ]

    session.add_all(associacoes)
    print("Associações de autores com livros inseridas com sucesso!")

    session.commit()
    session.close()

    # Criar Funcionarios
    criar_funcionario(nickname='admin', senha='admin', matricula='2111001', permissao='1',
                      data_contratacao='2020-01-01')
    criar_funcionario(nickname='bibliotecario', senha='123456', matricula='2111002', permissao='2',
                      data_contratacao='2020-01-01')

    criar_professor(nickname='jeremias', senha='123456', matricula='2111003', permissao='3',
                    data_contratacao='2020-01-01', regime_trabalho='40',
                    curso_descricao='Ciência da Computação')
    criar_professor(nickname='lucas', senha='123456', matricula='2111004', permissao='3',
                    data_contratacao='2020-01-01', regime_trabalho='40',
                    curso_descricao='Engenharia da Software')

    criar_aluno(nickname='aluno', senha='123456', matricula='2111005', permissao='3',
                data_ingresso='2020-01-01', data_previsao_conclusao='2020-01-01',
                curso_descricao='Ciência da Computação')
    criar_aluno(nickname='aluno2', senha='123456', matricula='2111006', permissao='3',
                data_ingresso='2020-01-01', data_previsao_conclusao='2020-01-01',
                curso_descricao='Engenharia da Software')
    criar_aluno(nickname='aluno3', senha='123456', matricula='2111007', permissao='3',
                data_ingresso='2020-01-01', data_previsao_conclusao='2020-01-01',
                curso_descricao='Ciência da Computação')
    criar_aluno(nickname='aluno4', senha='123456', matricula='2111008', permissao='4',
                data_ingresso='2020-01-01', data_previsao_conclusao='2020-01-01',
                curso_descricao='Engenharia da Software')
    criar_aluno(nickname='aluno5', senha='123456', matricula='2111009', permissao='4',
                data_ingresso='2020-01-01', data_previsao_conclusao='2020-01-01',
                curso_descricao='Ciência da Computação')
    criar_aluno(nickname='aluno6', senha='123456', matricula='2111010', permissao='4',
                data_ingresso='2020-01-01', data_previsao_conclusao='2020-01-01',
                curso_descricao='Engenharia da Software')

    criar_emprestimo(status_emprestimo='1', data_emprestimo='2020-01-01',
                     data_devolucao='2020-01-01', usuario_id='1', livro_id='1')
    criar_emprestimo(status_emprestimo='1', data_emprestimo='2020-01-01',
                     data_devolucao='2020-01-01', usuario_id='2', livro_id='2')
    criar_emprestimo(status_emprestimo='1', data_emprestimo='2020-01-01',
                     data_devolucao='2020-01-01', usuario_id='3', livro_id='3')
    criar_emprestimo(status_emprestimo='1', data_emprestimo='2020-01-01',
                     data_devolucao='2020-01-01', usuario_id='4', livro_id='4')
    criar_emprestimo(status_emprestimo='1', data_emprestimo='2020-01-01',
                     data_devolucao='2020-01-01', usuario_id='5', livro_id='5')
    criar_emprestimo(status_emprestimo='1', data_emprestimo='2020-01-01',
                     data_devolucao='2020-01-01', usuario_id='6', livro_id='6')
    criar_emprestimo(status_emprestimo='1', data_emprestimo='2020-01-01',
                     data_devolucao='2020-01-01', usuario_id='7', livro_id='7')
    criar_emprestimo(status_emprestimo='1', data_emprestimo='2020-01-01',
                     data_devolucao='2020-01-01', usuario_id='8', livro_id='8')
    criar_emprestimo(status_emprestimo='1', data_emprestimo='2020-01-01',
                     data_devolucao='2020-01-01', usuario_id='9', livro_id='9')
    criar_emprestimo(status_emprestimo='1', data_emprestimo='2020-01-01',
                     data_devolucao='2020-01-01', usuario_id='10', livro_id='10')

    print("Banco de dados inicializado e populado com sucesso!")


if __name__ == '__main__':
    main()
