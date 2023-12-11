from app.controller.ReservaController import ReservasController


def cadastrar_reserva():
    print("\n--- Cadastrar Nova Reserva ---")
    status_reserva = input("Status da reserva: ")
    data_reserva = input("Data da reserva (formato YYYY-MM-DD): ")
    Livros_idLivros = int(input("ID do livro reservado: "))
    Usuarios_idUsuarios = int(input("ID do usuário que fez a reserva: "))

    nova_reserva = ReservasController.criar_reserva(status_reserva, data_reserva, Usuarios_idUsuarios, Livros_idLivros)

    if nova_reserva:
        print("Reserva cadastrada com sucesso!")
    else:
        print("Erro ao cadastrar reserva.")


def atualizar_reserva():
    print("\n--- Atualizar Reserva ---")
    id_reserva = int(input("ID da reserva a ser atualizada: "))
    reserva = ReservasController.buscar_reserva(id_reserva)

    if reserva:
        print("Deixar em branco para manter o mesmo valor.")
        status_reserva = input(f"Status da reserva [{reserva.status_reserva}]: ") or reserva.status_reserva
        data_reserva = input(f"Data da reserva [{reserva.data_reserva}]: ") or reserva.data_reserva
        Livros_idLivros = int(input(f"ID do livro reservado [{reserva.Livros_idLivros}]: ")) or reserva.Livros_idLivros
        Usuarios_idUsuarios = int(
            input(f"ID do usuário que fez a reserva [{reserva.Usuarios_idUsuarios}]: ")) or reserva.Usuarios_idUsuarios

        ReservasController.atualizar_reserva(id_reserva, status_reserva=status_reserva, data_reserva=data_reserva,
                                             Livros_idLivros=Livros_idLivros, Usuarios_idUsuarios=Usuarios_idUsuarios)
        print("Reserva atualizada com sucesso!")
    else:
        print("Reserva não encontrada.")


atualizar_reserva()
