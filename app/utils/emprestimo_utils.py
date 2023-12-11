from app.controller.EmprestimoController import EmprestimosController 
from app.utils.livro_utils import listar_livros 
from app.controller.LivrosController import LivroController

def cadastrar_emprestimo(usuario_logado):
    
    
    listar_livros()
    status_emprestimo = "Emprestimo"
    print("\n--- Cadastrar Novo Empréstimo ---")
    escolha = input("nome do livro : ")
    livro = LivroController.buscar_livro_por_titulo(escolha)
    data_emprestimo = input("Data do empréstimo (YYYY-MM-DD): ")
    data_devolucao = input("Data de devolução (YYYY-MM-DD): ")
    
    

    novo_emprestimo = EmprestimosController.criar_emprestimo(status_emprestimo, data_emprestimo, data_devolucao, usuario_logado, livro.idLivros)

    if novo_emprestimo:
        print("Empréstimo cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar empréstimo.")

def atualizar_emprestimo():
    print("\n--- Atualizar Empréstimo ---")
    id_emprestimo = int(input("id do emprestimo : "))
    emprestimo = EmprestimosController.buscar_emprestimo(id_emprestimo)
    
    if emprestimo:
        print("Deixe em branco para manter o mesmo valor.")
        status_emprestimo = input(f"Status [{emprestimo.status_emprestimo}]: ") or emprestimo.status_emprestimo
        data_emprestimo = input(f"Data de Empréstimo [{emprestimo.data_emprestimo}]: ") or emprestimo.data_emprestimo
        data_devolucao = input(f"Data de Devolução [{emprestimo.data_devolucao}]: ") or emprestimo.data_devolucao
        
        EmprestimosController.atualizar_emprestimo(id_emprestimo, status_emprestimo=status_emprestimo, data_emprestimo=data_emprestimo, data_devolucao=data_devolucao)
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
    id_emprestimo = int(input("ID do empréstimo a ser removido: "))
    EmprestimosController.deletar_emprestimo(id_emprestimo)
    print("Empréstimo removido com sucesso.")
remover_emprestimo()
