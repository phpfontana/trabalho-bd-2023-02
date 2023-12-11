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

def atualizar_reserva():
    print("\n--- Atualizar Reserva ---")
    id_reserva = int(input("ID da reserva a ser atualizada: "))
    reserva = ReservasController.buscar_reserva(id_reserva)
    
    if reserva:
        print("Deixe em branco para manter o mesmo valor.")

        status_reserva = input(f"Status da reserva [{reserva.status_reserva}]: ")
        status_reserva = status_reserva if status_reserva.strip() else reserva.status_reserva

        data_reserva = input(f"Data da reserva [{reserva.data_reserva}]: ")
        data_reserva = data_reserva if data_reserva.strip() else reserva.data_reserva

        Livros_idLivros = input(f"ID do livro reservado [{reserva.Livros_idLivros}]: ")
        Livros_idLivros = int(Livros_idLivros) if Livros_idLivros.strip() else reserva.Livros_idLivros

        Usuarios_idUsuarios = input(f"ID do usuário que fez a reserva [{reserva.Usuarios_idUsuarios}]: ")
        Usuarios_idUsuarios = int(Usuarios_idUsuarios) if Usuarios_idUsuarios.strip() else reserva.Usuarios_idUsuarios

        ReservasController.atualizar_reserva(id_reserva, status_reserva=status_reserva, data_reserva=data_reserva, Livros_idLivros=Livros_idLivros, Usuarios_idUsuarios=Usuarios_idUsuarios)
        print("Reserva atualizada com sucesso!")
    else:
        print("Reserva não encontrada.")

def remover_reserva():
    print("\n--- Remover Reserva ---")
    id_reserva = int(input("ID da reserva a ser removida: "))
    ReservasController.deletar_reserva(id_reserva)
    print("Reserva removida com sucesso.")


def listar_reservas():
    print("\n--- Lista de Reservas ---")
    reservas = ReservasController.buscar_reservas()
    for reserva in reservas:
        print(
            f"ID: {reserva.idReservas}, Status: {reserva.status_reserva}, Data: {reserva.data_reserva}, Livro ID: {reserva.Livros_idLivros}, Usuário ID: {reserva.Usuarios_idUsuarios}"
        )
atualizar_reserva()