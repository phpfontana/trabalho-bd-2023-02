from sqlalchemy.exc import IntegrityError, NoResultFound

from app.controller.AutorController import AutorController

def cadastrar_autor():
    print("\n--- Cadastrar Novo Autor ---")
    nome = input("Nome do autor: ")
    cpf = input("CPF: ")
    nacionalidade = input("Nacionalidade: ")

    novo_autor = AutorController.criar_autor(nome, cpf, nacionalidade)

    if novo_autor:
        print("Autor cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar autor.")

def atualizar_autor():
    print("\n--- Atualizar Autor ---")
    nome_autor = input("Nome do autor a ser atualizado: ")
    autor = AutorController.buscar_autor_por_nome(nome_autor)  
    if autor:
        print("Deixar em branco para manter o mesmo valor.")
        novo_nome = input(f"Novo nome [{autor.nome}]: ") or autor.nome
        cpf = input(f"Novo CPF [{autor.cpf}]: ") or autor.cpf
        nacionalidade = input(f"Nova nacionalidade [{autor.nacionalidade}]: ") or autor.nacionalidade

        
        AutorController.atualizar_autor(autor.id_autor, nome=novo_nome, cpf=cpf, nacionalidade=nacionalidade)
        print("Autor atualizado com sucesso!")
    else:
        print("Autor não encontrado.")

def listar_autores():
    print("\n--- Lista de Autores ---")
    autores = AutorController.buscar_autores()
    for autor in autores:
        print(f"Nome: {autor.nome}, CPF: {autor.cpf}, Nacionalidade: {autor.nacionalidade}")

def remover_autor():
    print("\n--- Remover Autor ---")
    nome_autor = input("Nome do autor a ser removido: ")
    autor = AutorController.buscar_autor_por_nome(nome_autor)
    if autor:
        AutorController.deletar_autor(autor.id_autor)
        print("Autor removido com sucesso.")
    else:
        print("Autor não encontrado.")

remover_autor()