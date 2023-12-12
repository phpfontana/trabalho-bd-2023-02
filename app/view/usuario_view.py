from app.utils.autor_utils import listar_autores
from app.utils.livro_utils import listar_livros


def menu_usuario(usuario):
    while True:
        print("\n--- Menu do Administrador ---")
        print("1. Consultar Livros")
        print("2. Consultar Autores")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_livros()
        elif opcao == '2':
            listar_autores()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
