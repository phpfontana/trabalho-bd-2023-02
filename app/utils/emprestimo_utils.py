from app.controller.EmprestimoController import EmprestimosController
from app.controller.UsuarioController import UsuarioController
from app.utils.livro_utils import listar_livros
from app.controller.LivrosController import LivroController
from app.utils.usuario_utils import listar_usuarios


def cadastrar_emprestimo():
    print("\n--- Cadastrar Novo Empréstimo ---")

    # Listar usuários e selecionar um usuário por nickname
    listar_usuarios()

    # Buscar usuário pelo nickname
    nickname_usuario = input("Digite o nickname do usuário: ")
    usuario = UsuarioController.buscar_usuario_por_nome(nickname_usuario)

    if not usuario:
        print("Usuário não encontrado.")
        return

    # Listar livros disponíveis e selecionar um livro por título
    listar_livros()
    titulo_livro = input("Digite o título do livro: ")
    livro = LivroController.buscar_livro_por_titulo(titulo_livro)

    if not livro:
        print("Livro não encontrado.")
        return

    # Verificar se a quantidade do livro é suficiente para o empréstimo
    if livro.quantidade <= 0:
        print("Quantidade insuficiente do livro para empréstimo.")
        return

    # Obter informações do empréstimo
    data_emprestimo = input("Data do empréstimo (YYYY-MM-DD): ")
    data_devolucao = input("Data de devolução (YYYY-MM-DD): ")

    # Criar o empréstimo e atualizar a quantidade do livro
    status_emprestimo = "1"  # Emprestado
    novo_emprestimo = EmprestimosController.criar_emprestimo(status_emprestimo, data_emprestimo, data_devolucao,
                                                             usuario.idUsuarios, livro.idLivros)

    if novo_emprestimo:
        # Reduzir a quantidade do livro e atualizá-lo
        livro.quantidade -= 1
        LivroController.atualizar_livro(livro.idLivros, quantidade=livro.quantidade)
        print("Empréstimo cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar empréstimo.")


def atualizar_emprestimo():
    print("\n--- Atualizar Empréstimo ---")
    id_emprestimo = int(input("id do emprestimo : "))
    emprestimo = EmprestimosController.buscar_emprestimo(id_emprestimo)

    if emprestimo:
        print("Deixe em branco para manter o mesmo valor.")
        status_emprestimo = input(f"Status [{emprestimo.status_emprestimo}] (1 - Emprestado, 2 - Finalizado): ") or \
                            emprestimo.status_emprestimo
        data_emprestimo = input(f"Data de Empréstimo [{emprestimo.data_emprestimo}]: ") or emprestimo.data_emprestimo
        data_devolucao = input(f"Data de Devolução [{emprestimo.data_devolucao}]: ") or emprestimo.data_devolucao

        # Atualiza o empréstimo
        EmprestimosController.atualizar_emprestimo(id_emprestimo, status_emprestimo=status_emprestimo,
                                                   data_emprestimo=data_emprestimo, data_devolucao=data_devolucao)

        # Se o status foi alterado para "Finalizado", atualiza a quantidade do livro
        if status_emprestimo == "2" and emprestimo.status_emprestimo != "2":
            id_livro = emprestimo.Livros_idLivros
            livro = LivroController.buscar_livro_por_id(id_livro)
            if livro:
                livro.quantidade += 1
                LivroController.atualizar_livro(livro.idLivros, quantidade=livro.quantidade)

        print("Empréstimo atualizado com sucesso!")
    else:
        print("Empréstimo não encontrado.")


def listar_emprestimos():
    print("\n--- Lista de Empréstimos ---")
    emprestimos = EmprestimosController.buscar_emprestimos()
    for emprestimo in emprestimos:
        print(
            f"ID: {emprestimo.idEmprestimos}, Status: {emprestimo.status_emprestimo}, Data Empréstimo: {emprestimo.data_emprestimo}, Data Devolução: {emprestimo.data_devolucao}, ID do Usuário: {emprestimo.Usuarios_idUsuarios}, ID do Livro: {emprestimo.Livros_idLivros}")


def remover_emprestimo():
    print("\n--- Remover Empréstimo ---")
    # Listar empréstimos e selecionar um empréstimo por ID
    listar_emprestimos()

    # Obter o ID do empréstimo
    id_emprestimo = int(input("ID do empréstimo a ser removido: "))

    # Buscar o empréstimo
    emprestimo = EmprestimosController.buscar_emprestimo(id_emprestimo)

    if not emprestimo:
        print("Empréstimo não encontrado.")
        return

    # Obter o ID do livro associado ao empréstimo
    id_livro = emprestimo.Livros_idLivros

    # Remover o empréstimo
    EmprestimosController.deletar_emprestimo(id_emprestimo)

    # Buscar o livro associado ao empréstimo e aumentar sua quantidade
    livro = LivroController.buscar_livro_por_id(id_livro)
    if livro:
        livro.quantidade += 1
        LivroController.atualizar_livro(livro.idLivros, quantidade=livro.quantidade)

    print("Empréstimo removido com sucesso.")
