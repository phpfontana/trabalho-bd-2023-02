from app.controller.UsuarioController import UsuarioController
from app.utils.utils import login
from app.view.admin_view import menu_administrador
from app.view.usuario_autenticado_view import menu_usuario_autenticado


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
