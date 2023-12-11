from sqlalchemy.exc import IntegrityError, NoResultFound

from app.controller.AutorController import AutorController
from app.controller.LivrosController import LivroController
from app.model.models import AutoresDosLivros
from app.utils.utils import get_session


def cadastrar_livro():
    print("\n--- Cadastrar Novo Livro ---")
    titulo = input("Título do livro: ")
    isbn = input("ISBN: ")
    ano = int(input("Ano: "))
    editora = input("Editora: ")
    quantidade = int(input("Quantidade: "))
    categoria = input("Categoria: ")

    novo_livro = LivroController.criar_livro(titulo, isbn, ano, editora, quantidade, categoria)

    if novo_livro:
        print("Livro cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar livro.")


def atualizar_livro():
    print("\n--- Atualizar Livro ---")
    id_livro = int(input("ID do livro a ser atualizado: "))
    livro = LivroController.buscar_livro_por_id(id_livro)
    if livro:
        print("Deixar em branco para manter o mesmo valor.")
        titulo = input(f"Título [{livro.titulo}]: ") or livro.titulo
        isbn = input(f"ISBN [{livro.ISBN}]: ") or livro.ISBN
        ano = input(f"Ano [{livro.ano}]: ") or livro.ano
        editora = input(f"Editora [{livro.editora}]: ") or livro.editora
        quantidade = input(f"Quantidade [{livro.quantidade}]: ") or livro.quantidade
        Categoria = input(f"Categoria [{livro.Categoria}]: ") or livro.Categoria

        LivroController.atualizar_livro(id_livro, titulo=titulo, ISBN=isbn, ano=ano, editora=editora,
                                        quantidade=quantidade, Categoria=Categoria)
        print("Livro atualizado com sucesso!")
    else:
        print("Livro não encontrado.")


def remover_livro():
    print("\n--- Remover Livro ---")
    id_livro = int(input("ID do livro a ser removido: "))
    LivroController.deletar_livro(id_livro)
    print("Livro removido com sucesso.")


def listar_livros():
    print("\n--- Lista de Livros ---")
    livros = LivroController.buscar_livros()
    for livro in livros:
        print(
            f"ID: {livro.idLivros}, Título: {livro.titulo}, ISBN: {livro.ISBN}, Ano: {livro.ano}, Editora: {livro.editora}, Quantidade: {livro.quantidade}, Categoria: {livro.Categoria}")


def associar_autores_livro_por_nome():
    print("\n--- Associar Autores a Livro por Nome ---")
    titulo_livro = input("Título do livro: ")
    livro = LivroController.buscar_livro_por_titulo(titulo_livro)

    if livro:
        autores_associados = []
        while True:
            nome_autor = input("Nome do autor (deixe em branco para terminar): ")
            if nome_autor == "":
                break
            autor = AutorController.buscar_autor_por_nome(nome_autor)
            if autor:
                autores_associados.append(autor)
                print(f"Autor '{nome_autor}' será associado ao livro '{titulo_livro}'.")
            else:
                print(f"Autor '{nome_autor}' não encontrado.")

        if autores_associados:
            session = get_session()
            try:
                for autor in autores_associados:
                    nova_associacao = AutoresDosLivros(Autores_id_autor=autor.id_autor, Livros_idLivros=livro.idLivros)
                    session.add(nova_associacao)
                session.commit()
                print(f"Todos os autores foram associados ao livro '{titulo_livro}' com sucesso!")
            except IntegrityError as e:
                session.rollback()
                print(f"Erro ao associar autores ao livro: {e}")
            finally:
                session.close()
    else:
        print(f"Livro '{titulo_livro}' não encontrado.")


def remover_associacao_autor_livro():
    print("\n--- Remover Associação Autor-Livro ---")
    titulo_livro = input("Título do livro: ")
    livro = LivroController.buscar_livro_por_titulo(titulo_livro)

    if livro:
        nome_autor = input("Nome do autor a desassociar: ")
        autor = AutorController.buscar_autor_por_nome(nome_autor)

        if autor:
            session = get_session()
            try:
                # Buscar a associação específica
                associacao = session.query(AutoresDosLivros).filter_by(Autores_id_autor=autor.id_autor,
                                                                       Livros_idLivros=livro.idLivros).one()
                session.delete(associacao)
                session.commit()
                print(f"Autor '{nome_autor}' foi desassociado do livro '{titulo_livro}' com sucesso!")
            except NoResultFound:
                print(f"A associação entre o autor '{nome_autor}' e o livro '{titulo_livro}' não existe.")
            except Exception as e:
                session.rollback()
                print(f"Erro ao desassociar autor do livro: {e}")
            finally:
                session.close()
        else:
            print(f"Autor '{nome_autor}' não encontrado.")
    else:
        print(f"Livro '{titulo_livro}' não encontrado.")
