from sqlalchemy.exc import IntegrityError, NoResultFound

from app.controller.AlunoController import AlunoController
from app.controller.FuncionarioController import FuncionarioController
from app.controller.ProfessorController import ProfessorController
from app.controller.UsuarioController import UsuarioController
from app.model.models import AutoresDosLivros
from app.utils.utils import get_session


def cadastrar_funcionario():
    print("\n--- Cadastrar Novo Funcionário ---")

    # Obter dados do usuário
    nickname = input("Nickname: ")
    senha = input("Senha: ")
    matricula = input("Matrícula: ")
    permissao = input("Permissão: ")
    data_contratacao = input("Data de contratação (AAAA-MM-DD): ")

    # Validações dos dados podem ser implementadas aqui

    try:
        # Tentar criar o funcionário utilizando o controller
        funcionario_criado = FuncionarioController.criar_funcionario(nickname, senha, matricula, permissao,
                                                                     data_contratacao)
        print(f"Funcionário  criado com sucesso!")
    except IntegrityError as e:
        print(f"Erro ao criar o funcionário: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def cadastrar_aluno():
    print("\n--- Cadastrar Novo Aluno ---")

    # Obter dados do usuário
    nickname = input("Nickname: ")
    senha = input("Senha: ")
    matricula = input("Matrícula: ")
    permissao = input("Permissão: ")

    # Obter dados específicos do aluno
    data_ingresso = input("Data de ingresso (AAAA-MM-DD): ")
    data_previsao_conclusao = input("Data de previsão de conclusão (AAAA-MM-DD): ")
    curso_descricao = input("Descrição do curso: ")

    # Validações dos dados podem ser implementadas aqui

    try:
        # Tentar criar o aluno utilizando o controller
        aluno_criado = AlunoController.criar_aluno(nickname, senha, matricula, permissao,
                                                   data_ingresso, data_previsao_conclusao, curso_descricao)
        print(f"Aluno criado com sucesso! ID: {aluno_criado.idAluno}")
    except IntegrityError as e:
        print(f"Erro ao criar o aluno: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def cadastrar_professor():
    print("\n--- Cadastrar Novo Professor ---")

    # Obter dados do usuário
    nickname = input("Nickname: ")
    senha = input("Senha: ")
    matricula = input("Matrícula: ")
    permissao = input("Permissão: ")

    # Obter dados específicos do professor
    data_contratacao = input("Data de contratação (AAAA-MM-DD): ")
    regime_trabalho = input("Regime de trabalho: ")
    curso_descricao = input("Descrição do curso: ")

    # Validações dos dados podem ser implementadas aqui

    try:
        # Tentar criar o professor utilizando o controller
        professor_criado = ProfessorController.criar_professor(nickname, senha, matricula, permissao,
                                                               data_contratacao, regime_trabalho, curso_descricao)
        print(f"Professor criado com sucesso! ID: {professor_criado.idProfessor}")
    except IntegrityError as e:
        print(f"Erro ao criar o professor: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def atualizar_funcionario():
    print("\n--- Atualizar Funcionário ---")

    id_usuario = input("Digite o ID do usuário do funcionário a ser atualizado: ")

    # Verifica se o funcionário existe
    funcionario_existente = FuncionarioController.buscar_funcionario_por_usuario_id(id_usuario)
    if not funcionario_existente:
        print("Funcionário não encontrado.")
        return

    id_funcionario = funcionario_existente.idFuncionario

    # Dados do usuário
    nickname = input("Digite o novo nickname (deixe em branco para manter o atual): ")
    senha = input("Digite a nova senha (deixe em branco para manter a atual): ")
    matricula = input("Digite a nova matricula (deixe em branco para manter a atual): ")
    permissao = input("Digite a nova permissão (deixe em branco para manter a atual): ")

    # Dados específicos do funcionário
    data_contratacao = input("Digite a nova data de contratação (YYYY-MM-DD) (deixe em branco para manter a atual): ")

    usuario_updates = {}
    if nickname:
        usuario_updates["nickname"] = nickname
    if senha:
        usuario_updates["senha"] = senha
    if matricula:
        usuario_updates["matricula"] = matricula
    if permissao:
        usuario_updates["permissao"] = permissao

    funcionario_updates = {}
    if data_contratacao:
        funcionario_updates["data_contratacao"] = data_contratacao

    try:
        # Atualiza o usuário e o funcionário
        if usuario_updates:
            UsuarioController.atualizar_usuario(id_usuario, **usuario_updates)
        if funcionario_updates:
            FuncionarioController.atualizar_funcionario(id_funcionario, **funcionario_updates)
        print("Funcionário atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar funcionário: {e}")


def atualizar_aluno():
    print("\n--- Atualizar Aluno ---")

    id_usuario = input("Digite o ID do usuário do aluno a ser atualizado: ")

    # Verifica se o aluno existe
    aluno_existente = AlunoController.buscar_aluno_por_usuario_id(id_usuario)
    if not aluno_existente:
        print("Aluno não encontrado.")
        return

    id_aluno = aluno_existente.idAluno

    # Dados do usuário
    nickname = input("Digite o novo nickname (deixe em branco para manter o atual): ")
    senha = input("Digite a nova senha (deixe em branco para manter a atual): ")
    matricula = input("Digite a nova matricula (deixe em branco para manter a atual): ")
    permissao = input("Digite a nova permissão (deixe em branco para manter a atual): ")

    # Dados específicos do aluno
    data_ingresso = input("Digite a nova data de ingresso (YYYY-MM-DD) (deixe em branco para manter a atual): ")
    data_previsao_conclusao = input(
        "Digite a nova data de previsão de conclusão (YYYY-MM-DD) (deixe em branco para manter a atual): ")
    curso_descricao = input("Digite a descrição do novo curso (deixe em branco para manter o atual): ")

    usuario_updates = {}
    if nickname:
        usuario_updates["nickname"] = nickname
    if senha:
        usuario_updates["senha"] = senha
    if matricula:
        usuario_updates["matricula"] = matricula
    if permissao:
        usuario_updates["permissao"] = permissao

    aluno_updates = {}
    if data_ingresso:
        aluno_updates["data_ingresso"] = data_ingresso
    if data_previsao_conclusao:
        aluno_updates["data_previsao_conclusao"] = data_previsao_conclusao
    if curso_descricao:
        aluno_updates["Curso_idCurso"] = curso_descricao

    try:
        # Atualiza o usuário e o aluno
        if usuario_updates:
            UsuarioController.atualizar_usuario(id_usuario, **usuario_updates)
        if aluno_updates:
            AlunoController.atualizar_aluno(id_aluno, **aluno_updates)
        print("Aluno atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar aluno: {e}")


def atualizar_professor():
    print("\n--- Atualizar Professor ---")

    id_usuario = input("Digite o ID do usuário do professor a ser atualizado: ")

    # Verifica se o professor existe
    professor_existente = ProfessorController.buscar_professor_por_usuario_id(id_usuario)
    if not professor_existente:
        print("Professor não encontrado.")
        return

    id_professor = professor_existente.idProfessor

    # Dados do usuário
    nickname = input("Digite o novo nickname (deixe em branco para manter o atual): ")
    senha = input("Digite a nova senha (deixe em branco para manter a atual): ")
    matricula = input("Digite a nova matricula (deixe em branco para manter a atual): ")
    permissao = input("Digite a nova permissão (deixe em branco para manter a atual): ")

    # Dados específicos do professor
    data_contratacao = input("Digite a nova data de contratação (YYYY-MM-DD) (deixe em branco para manter a atual): ")
    regime_trabalho = input("Digite o novo regime de trabalho (deixe em branco para manter o atual): ")
    curso_descricao = input("Digite a descrição do novo curso (deixe em branco para manter o atual): ")

    usuario_updates = {}
    if nickname:
        usuario_updates["nickname"] = nickname
    if senha:
        usuario_updates["senha"] = senha
    if matricula:
        usuario_updates["matricula"] = matricula
    if permissao:
        usuario_updates["permissao"] = permissao

    professor_updates = {}
    if data_contratacao:
        professor_updates["data_contratacao"] = data_contratacao
    if regime_trabalho:
        professor_updates["regime_trabalho"] = regime_trabalho
    if curso_descricao:
        professor_updates["Curso_idCurso"] = curso_descricao

    try:
        # Atualiza o usuário e o professor
        if usuario_updates:
            UsuarioController.atualizar_usuario(id_usuario, **usuario_updates)
        if professor_updates:
            ProfessorController.atualizar_professor(id_professor, **professor_updates)
        print("Professor atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar professor: {e}")


def remover_usuario():
    print("\n--- Remover Usuário ---")

    # Obter o ID do usuário a ser removido
    try:
        id_usuario = int(input("Digite o ID do usuário que deseja remover: "))
    except ValueError:
        print("Por favor, insira um número válido para o ID.")
        return

    try:
        # Tentar remover o usuário utilizando o controller
        UsuarioController.deletar_usuario(id_usuario)
        print(f"Usuário com ID {id_usuario} foi removido com sucesso!")
    except NoResultFound:
        print(f"Nenhum usuário encontrado com o ID {id_usuario}.")
    except IntegrityError as e:
        print(f"Erro ao remover o usuário: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def listar_usuarios():
    print("\n--- Lista de Usuários ---")
    # Chamada ao controller para listar os usuários
    usuarios = UsuarioController.buscar_usuarios()

    for usuario in usuarios:
        print(
            f"ID: {usuario.idUsuarios} - Nome: {usuario.nickname} - Matricula: {usuario.matricula} - Permissao: {usuario.permissao}")
