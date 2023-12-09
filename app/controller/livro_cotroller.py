from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import Session
from models import Base
from sqlalchemy.ext.declarative import declarative_base

class livro_controller:

    def __init__(self, session: Session):
        self.session = session

    def cadastrar_livro(self titulo, isbn, ano, editora, quantidade_copias, categoria):
        novo_livro = Livro (

            isbn=isbn,
            titulo=titulo,
            ano=ano,
            editora=editora,
            quantidade_copias=quantidade_copias,
            categoria=categoria
            emprestado = 'nao'

        )
        self.session.add(novo_livro)
        self.session.commit()

    def atualizar_livro(self, livro_id):
        # Encontrar o livro pelo ID
        livro = self.session.query(Livro).filter_by(idLivros=livro_id).first()

        # Verificar se o livro existe
        if livro:
            print("Atualizando informações do livro ID:", livro_id)

            while True:
                # Exibir opções de informações para atualizar
                print("\nEscolha a informação a ser atualizada:")
                print("1. Título")
                print("2. ISBN")
                print("3. Ano")
                print("4. Editora")
                print("5. Quantidade de Cópias")
                print("6. Categoria")
                print("0. Sair")

                escolha = input("Digite o número da opção desejada: ")

                if escolha == "0":
                    print("Atualização concluída.")
                    break

                if escolha == "1":
                    novo_titulo = input("Digite um novo titulo")
                    setattr(livro, "nome", novo_titulo)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                if escolha == "2":
                    novo_isbn = input("Digite um novo ISBN")
                    setattr(livro, "ISBN", novo_isbn)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                if escolha == "3":
                    novo_ano = input("Digite um novo ano")
                    setattr(livro, "ano", novo_ano)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                if escolha == "4":
                    nova_editora = input("Digite uma nova editora")
                    setattr(livro, "editora", nova_editora)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                if escolha == "5":
                    nova_editora = input("Digite uma nova editora")
                    setattr(livro, "editora", nova_editora)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                if escolha == "6":
                    nova_cat = input("Digite uma nova categoria")
                    setattr(livro, "Categoria", nova_cat)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                else:
                    print("Opção inválida. Tente novamente.")
        else:
            print("Livro não encontrado.")
    
    def remover_livro(self,livro_id):
        livro = self.session.query(Livro).filter_by(idLivros=livro_id).first()

        if livro:
            self.session.delete(livro)

            self.session.commit()

            return 'Livro excluido com sucesso'
        else:
            return 'Erro ao excluir livro'

    def ler_livros(self):
        

        livros = self.session.query(Livro).all()

        
        if livros:
            # Imprime indices da tabela
            print("{:<5} {:<20} {:<15} {:<10} {:<15}".format("ID", "Título", "ISBN", "Ano", "Editora"))
            print("-" * 60)

            # Imprime informação dos livros
            for livro in livros:
                print("{:<5} {:<20} {:<15} {:<10} {:<15}".format(
                    livro.idLivros, livro.titulo, livro.ISBN, livro.ano, livro.editora
                ))
        else:
            print("Nenhum livro encontrado na tabela.")
    

