from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import Session
from models import Base
from sqlalchemy.ext.declarative import declarative_base

class autor_controller:

    def __init__(self, session: Session):
        self.session = session

    def cadastrar_autor(self , nome, cpf, nacionalidade):
        novo_autor = Autor (

            nome = nome
            cpf = cpf
            nacionalidade = nacionalidade

        )
        self.session.add(novo_autor)
        self.session.commit()

    def atualizar_autor(self,autor_id):
        # Encontrar o autor pelo ID
        autor = self.session.query(Autor).filter_by(idAutor=autor_id).first()

        if autor:
            print("Atualizando informações do autor ID:", autor_id)

            while True:
                print("\nEscolha a informação a ser atualizada:")
                print("1. Nome")
                print("2. CPF")
                print("3. Nacionalidade")
                print("0. Sair")
        
                escolha = input("Digite o número da opção desejada: ")

                if escolha == "0" :
                    print("Atualização concluída.")
                    break
                
                if escolha == "1":
                    novo_nome = input("Digite o novo nome")
                    setattr(autor, "nome", novo_nome)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")
                
                if escolha == "2":
                    novo_cpf = input("Digite o novo CPF")
                    setattr(autor, "cpf", novo_cpf)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                if escolha == "3":
                    nova_nacionalidade = input("Digite a nova Nacionalidade")
                    setattr(autor, "nacionalidade", nova_nacionalidade)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")
                else:
                    print("Opção inválida. Tente novamente.")

        else:
            print("Livro não encontrado.")


                



        

        
    
    def remover_autor(self,autor_id):
        autor = self.session.query(Autor).filter_by(idAutor=autor_id).first()
        
        if autor:
            self.session.delete(autor)

            self.session.commit()

            return 'Autor excluido com sucesso'
        else:
            return 'Erro ao excluir autor'
    
    def ler_autores(self):
        # Consulta para recuperar todos os autores
        autores = self.session.query(Autor).all()

        # Verificar se há autores
        if autores:
            # Mostrar cabeçalho da tabela
            print("{:<5} {:<20} {:<15} {:<15}".format("ID", "Nome", "CPF", "Nacionalidade"))
            print("-" * 60)

            # Mostrar cada autor na tabela
            for autor in autores:
                print("{:<5} {:<20} {:<15} {:<15}".format(
                    autor.id_autor, autor.nome, autor.cpf, autor.nacionalidade
                ))
        else:
            print("Nenhum autor encontrado.")