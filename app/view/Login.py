import arquivo_funcoes


def Login():
    arquivo_funcoes.limpar_terminal()
    print("Bem Vindo")
    username = input("Digite o nome de usuário: ")
    usuario_existe, senha, tipo = arquivo_funcoes.verificar_usuario(username)
    if usuario_existe:
        arquivo_funcoes.limpar_terminal()
        password = input("Digite a senha: ")

        if password == senha:
            print("Login bem-sucedido!")
            arquivo_funcoes.limpar_terminal()
            arquivo_funcoes.redirecionar_usuario(tipo, username)
        else:
            arquivo_funcoes.limpar_terminal()
            print("Senha incorreta.")
            Login()
    else:
        arquivo_funcoes.limpar_terminal()
        print("Usuário não encontrado.")

        Login()


Login()
