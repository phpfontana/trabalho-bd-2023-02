from sys import platform
import os

def redirecionar_usuario(tipo_usuario, nome_usuario):
    if tipo_usuario == 'Autenticados':
        import Autenticados
        Autenticados.main_Autenticados(nome_usuario)
    elif tipo_usuario == 'Administrador':
        import Administrador
        Administrador.main_Administrador(nome_usuario)
    elif tipo_usuario == 'Bibliotecário':
        import Bibliotecario
        Bibliotecario.main_Bibliotecário(nome_usuario)
    elif tipo_usuario == 'Não Autenticados':
        import Não_Autenticados
        Não_Autenticados.main_Usuários_Autenticados(nome_usuario)
        
    else:
        print("Tipo de usuário não reconhecido.")

def verificar_usuario(username):
    #chamar o controller com as informaçoes nessesarias 
    #RETORNO se existe usuario, senha e o tipo do usuario
    # se não
    return True, '1234', "Autenticados"


def limpar_terminal():
    if platform == "win32":  
        os.system('cls')
    else:  
        os.system('clear')