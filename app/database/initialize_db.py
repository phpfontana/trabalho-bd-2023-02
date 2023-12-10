from sqlalchemy_utils import drop_database, database_exists, create_database
from app.model.models import Base  # Importe suas classes de modelo aqui
from app.utils.utils import get_engine_from_config, get_session


# Reinicializa o banco de dados
def reset_database():
    engine = get_engine_from_config()

    # Exclui o banco de dados se ele já existir
    if database_exists(engine.url):
        print(f"Excluindo o banco de dados existente: {engine.url}")
        drop_database(engine.url)

    # Cria o banco de dados
    print(f"Criando o banco de dados: {engine.url}")
    create_database(engine.url)

    # Cria todas as tabelas definidas nos modelos
    Base.metadata.create_all(engine)


# Main
def main():
    # Reinicializa o banco de dados
    reset_database()

    # Cria uma nova sessão
    session = get_session()

    # ... [Insira aqui o código para adicionar autores, livros, usuários e associações] ...

    # Commit final
    session.commit()
    print("Banco de dados inicializado e populado com sucesso!")

    # Fechar a sessão
    session.close()


if __name__ == '__main__':
    main()
