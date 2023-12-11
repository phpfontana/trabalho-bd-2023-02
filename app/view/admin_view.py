from app.utils.autor_utils import cadastrar_autor, atualizar_autor, remover_autor, listar_autores
from app.utils.livro_utils import cadastrar_livro, atualizar_livro, remover_livro, listar_livros, \
    associar_autores_livro_por_nome, remover_associacao_autor_livro
from app.utils.usuario_utils import listar_usuarios, remover_usuario, cadastrar_professor, \
    cadastrar_aluno, cadastrar_funcionario, atualizar_professor, atualizar_funcionario, atualizar_aluno


def menu_administrador(usuario_logado):
    while True:
        print("\n--- Menu do Administrador ---")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Autores")
        print("3. Gerenciar Usuários")
        print("4. Gerenciar Empréstimos")
        print("5. Gerenciar Reservas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gerenciar_livros()
        elif opcao == '2':
            gerenciar_autores()
        elif opcao == '3':
            gerenciar_usuarios()
        elif opcao == '4':
            gerenciar_emprestimos()
        elif opcao == '5':
            gerenciar_reservas()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


def gerenciar_livros():
    while True:
        print("\n--- Gerenciamento de Livros ---")
        print("1. Cadastrar Livro")
        print("2. Atualizar Livro")
        print("3. Remover Livro")
        print("4. Listar Livros")
        print("5. Associar Autores a Livro por Nome")
        print("6. Remover Associação Autor-Livro")
        print("0. Voltar para o menu anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            atualizar_livro()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            listar_livros()
        elif opcao == '5':
            associar_autores_livro_por_nome()
        elif opcao == '6':
            remover_associacao_autor_livro()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


def gerenciar_autores():
    while True:
        print("\n--- Gerenciamento de Autores ---")
        print("1. Cadastrar Autor")
        print("2. Atualizar Autor")
        print("3. Remover Autor")
        print("4. Listar Autores")
        print("0. Voltar para o menu anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_autor()
        elif opcao == '2':
            atualizar_autor()
        elif opcao == '3':
            remover_autor()
        elif opcao == '4':
            listar_autores()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


def gerenciar_usuarios():
    while True:
        print("\n--- Gerenciamento de Usuários ---")
        print("1. Cadastrar Usuario")
        print("2. Atualizar Usuario")
        print("3. Remover Usuário")
        print("4. Listar Usuários")
        print("0. Voltar para o menu anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            atualizar_usuario()
        elif opcao == '3':
            remover_usuario()
        elif opcao == '4':
            listar_usuarios()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


def cadastrar_usuario():
    print("\n--- Cadastrar Usuário ---")
    print("Escolha o tipo de usuário a ser cadastrado:")
    print("1. Funcionário")
    print("2. Aluno")
    print("3. Professor")
    tipo_escolha = input("Digite o número correspondente: ")

    if tipo_escolha == '1':
        cadastrar_funcionario()
    elif tipo_escolha == '2':
        cadastrar_aluno()
    elif tipo_escolha == '3':
        cadastrar_professor()
    else:
        print("Opção inválida. Tente novamente.")


def atualizar_usuario():
    print("\n--- Atualizar Usuário ---")
    print("Escolha o tipo de usuário a ser atualizado:")
    print("1. Funcionário")
    print("2. Aluno")
    print("3. Professor")
    tipo_escolha = input("Digite o número correspondente: ")

    if tipo_escolha == '1':
        atualizar_funcionario()
    elif tipo_escolha == '2':
        atualizar_aluno()
    elif tipo_escolha == '3':
        atualizar_professor()
    else:
        print("Opção inválida. Tente novamente.")
    pass

def gerenciar_emprestimos():
    # Implemente as funções para criar, atualizar e remover empréstimos
    pass


def gerenciar_reservas():
    # Implemente as funções para criar, atualizar e remover reservas
    pass


