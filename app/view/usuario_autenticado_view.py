from app.utils.autor_utils import listar_autores
from app.utils.emprestimo_utils import listar_emprestimos
from app.utils.livro_utils import listar_livros
from app.utils.reserva_utils import listar_reservas_do_usuario
from app.utils.reserva_utils import cadastrar_reserva_usuario

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
            listar_reservas_do_usuario(usuario)
        elif opcao == '5':
            cadastrar_reserva_usuario(usuario)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


