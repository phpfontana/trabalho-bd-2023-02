from app.utils.livro_utils import cadastrar_livro, atualizar_livro, remover_livro, listar_livros, \
    associar_autores_livro_por_nome, remover_associacao_autor_livro


def menu_administrador():
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
    # Implemente as funções para criar, atualizar e remover autores
    # Exemplo:
    # print("\n--- Gerenciamento de Autores ---")
    # print("1. Cadastrar Autor")
    # print("2. Atualizar Autor")
    # print("3. Remover Autor")
    # ...
    pass


def gerenciar_usuarios():
    # Implemente as funções para criar, atualizar e remover usuários
    pass


def gerenciar_emprestimos():
    # Implemente as funções para criar, atualizar e remover empréstimos
    pass


def gerenciar_reservas():
    # Implemente as funções para criar, atualizar e remover reservas
    pass


if __name__ == '__main__':
    menu_administrador()
