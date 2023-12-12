from app.utils.emprestimo_utils import cadastrar_emprestimo, atualizar_emprestimo, remover_emprestimo, \
    listar_emprestimos
from app.utils.reserva_utils import cadastrar_reserva, atualizar_reserva, remover_reserva, listar_reservas

def menu_bibliotecario(usuario):
    while True:
        print("\n--- Menu do Bibliotecario ---")
        print("1. Gerenciar Empréstimos")
        print("2. Gerenciar Reservas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gerenciar_emprestimos()
        elif opcao == '2':
            gerenciar_reservas()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


def gerenciar_emprestimos():
    while True:
        print("\n--- Gerenciamento de Empréstimos ---")
        print("1. Cadastrar Empréstimo")
        print("2. Atualizar Empréstimo")
        print("3. Remover Empréstimo")
        print("4. Listar Empréstimos")
        print("0. Voltar para o menu anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_emprestimo()
        elif opcao == '2':
            atualizar_emprestimo()
        elif opcao == '3':
            remover_emprestimo()
        elif opcao == '4':
            listar_emprestimos()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
        pass

def gerenciar_reservas():
    while True:
        print("\n--- Gerenciamento de Reservas ---")
        print("1. Cadastrar Reserva")
        print("2. Atualizar Reserva")
        print("3. Remover Reserva")
        print("4. Listar Reservas")
        print("0. Voltar para o menu anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_reserva()
        elif opcao == '2':
            atualizar_reserva()
        elif opcao == '3':
            remover_reserva()
        elif opcao == '4':
            listar_reservas()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
        pass
