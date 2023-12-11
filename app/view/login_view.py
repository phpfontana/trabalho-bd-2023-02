from getpass import getpass

from app.controller.UsuarioController import UsuarioController
from app.view.admin_view import menu_administrador
from app.view.usuario_autenticado_view import menu_usuario_autenticado


def login():
    print("Bem-vindo ao Sistema de Gerenciamento da Biblioteca")
    username = input('Nome de Usuário: ')
    password = input('Senha: ')

    usuario = UsuarioController.buscar_usuario_por_nome(username)

    if usuario and usuario.senha == password:  # Aqui deve-se implementar uma verificação de hash de senha
        print(f"Bem-vindo, {usuario.nickname}!")
        return usuario
    else:
        print("Usuário ou senha incorretos!")
        return None


def menu_bibliotecario():
    # Implementar o menu do bibliotecário
    pass


def main():
    usuario_logado = login()

    if usuario_logado:
        if usuario_logado.permissao == 'admin':  # Admin
            menu_administrador(usuario_logado)
        elif usuario_logado.permissao == '2':  # Bibliotecário
            menu_bibliotecario()
        elif usuario_logado.permissao == '3':  # Usuário Autenticado
            menu_usuario_autenticado(usuario_logado)
        else:
            print("Permissão desconhecida.")


if __name__ == "__main__":
    main()
