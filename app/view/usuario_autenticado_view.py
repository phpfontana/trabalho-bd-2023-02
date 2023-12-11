from app.utils.autor_utils import listar_autores
from app.utils.emprestimo_utils import listar_emprestimos
from app.utils.livro_utils import listar_livros


def consultar_reservas():
    pass


def realizar_reserva(usuario):
    pass


def menu_usuario_autenticado(usuario):
    while True:
        print("\n--- Menu do Usuário ---")
        print("1. Consultar Livros")
        print("2. Consultar Autores")
        print("3. Consultar Empréstimos")
        print("4. Consultar Reservas")
        print("5. Realizar Reserva")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_livros()
        elif opcao == '2':
            listar_autores()
        elif opcao == '3':
            listar_emprestimos()
        elif opcao == '4':
            consultar_reservas()
        elif opcao == '5':
            realizar_reserva(usuario)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

