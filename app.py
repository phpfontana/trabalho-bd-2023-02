from app.controller.UsuarioController import UsuarioController
from app.view.admin_view import menu_administrador
from app.view.usuario_autenticado_view import menu_usuario_autenticado
from app.utils.utils import login


def menu_bibliotecario():
    # Implementar o menu do bibliotecário
    pass


def menu_usuario_nao_autenticado(usuario_logado):
    pass


def main():
    usuario_logado = login()

    if usuario_logado:
        if usuario_logado.permissao == '1':  # Admin
            menu_administrador(usuario_logado)
        elif usuario_logado.permissao == '2':  # Bibliotecário
            menu_bibliotecario()
        elif usuario_logado.permissao == '3':  # Usuário Autenticado
            menu_usuario_autenticado(usuario_logado)
        elif usuario_logado.permissao == '4':  # Usuário não autenticado
            menu_usuario_nao_autenticado(usuario_logado)
        else:
            print("Permissão desconhecida.")


if __name__ == "__main__":
    main()
