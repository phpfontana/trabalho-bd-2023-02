from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import Session
from models import Base
from sqlalchemy.ext.declarative import declarative_base

class usuario_controller:

    def __init__(self, session: Session):
        self.session = session

    def cadastrar_usuario(self , nickname, senha, matricula):
    
        novo_usuario = Usuario (

            nickname = nickname
            senha = senha
            matricula = matricula
            permissao = "nenhuma"
            autenticados = False

        )
        self.session.add(novo_usuario)
        self.session.commit()

    def atualizar_usuario(self,usuario_id):
        usuario = self.session.query(Usuario).filter_by(idLivros=usuario_id).first()

        if usuario:

            while True:
                print("\nEscolha a informação a ser atualizada:")
                print("1. Nickname")
                print("2. Senha")
                print("3. Matricula")
                print("4. Permissao")
                # print("5. Autenticar usuario")
                print("0. Sair")

                escolha = input("Digite o número da opção desejada: ")

                if escolha == "0":
                    print("Atualização concluída.")
                    break

                if escolha == "1":
                    novo_nick = input("Digite um novo Nickname")
                    setattr(usuario, "nickname", novo_nick)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                if escolha == "2":
                    nova_senha = input("Digite uma nova Senha")
                    setattr(usuario, "senha", nova_senha)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                if escolha == "3":
                    nova_mat = input("Digite uma nova Matricula")
                    setattr(usuario, "matricula", nova_mat)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                if escolha == "4":
                    nova_perm = input("Digite a Permissao")
                    setattr(usuario, "permissao", nova_perm)
                    self.session.commit()
                    print("Informação atualizada com sucesso.")

                # if escolha == "5":
                    
                #     setattr(usuario, "autenticados", True)
                #     self.session.commit()
                #     print("Informação atualizada com sucesso.")

                else:
                    print("Opção inválida. Tente novamente.")
        else:
           print("Usuario não encontrado.") 
    
    def remover_usuario(self,usuario_id):
        usuario = self.session.query(Usuario).filter_by(idUsuario=usuario_id).first()

        if usuario:
            self.session.delete(usuario)

            self.session.commit()

            return "Usuario excluido com sucesso"
        else:
            return "Erro ao excluir usuario"

    def ler_usuarios(self):
        # Consulta para recuperar todos os usuários, sem mostrar a senha
        usuarios = self.session.query(Usuario.idUsuarios, Usuario.nickname, 
                                     Usuario.matricula, Usuario.permissao, 
                                     Usuario.autenticados).all()

        # Verificar se há usuários
        if usuarios:
            # Mostrar cabeçalho da tabela
            print("{:<5} {:<20} {:<15} {:<15} {:<10}".format(
                "ID", "Nickname", "Matrícula", "Permissão", "Autenticado"
            ))
            print("-" * 60)

            # Mostrar cada usuário na tabela
            for usuario in usuarios:
                print("{:<5} {:<20} {:<15} {:<15} {:<10}".format(
                    usuario.idUsuarios, usuario.nickname,
                    usuario.matricula, usuario.permissao, usuario.autenticados
                ))
        else:
            print("Nenhum usuário encontrado na tabela.")
    