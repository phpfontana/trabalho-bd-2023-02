from app.controller.ReservaController import ReservasController

def cadastrar_reserva():
    print("\n--- Cadastrar Nova Reserva ---")
    status_reserva = input("Status da reserva: ")
    data_reserva = input("Data da reserva (formato YYYY-MM-DD): ")
    Livros_idLivros = int(input("ID do livro reservado: "))
    Usuarios_idUsuarios = int(input("ID do usuário que fez a reserva: "))

    nova_reserva = ReservasController.criar_reserva(status_reserva, data_reserva,  Usuarios_idUsuarios, Livros_idLivros)

    if nova_reserva:
        print("Reserva cadastrada com sucesso!")
    else:
        print("Erro ao cadastrar reserva.")


cadastrar_reserva()