from sqlalchemy.exc import IntegrityError
from app.model.models import AutoresDosLivros, Livro
from app.utils.utils import get_session


class LivrosController:

    @staticmethod
    def criar_livro(titulo, isbn, ano, editora, quantidade, categoria, id_autores):
        """ Cria um novo livro e associa autores a ele. """
        session = get_session()

        try:
            # Cria um novo objeto Livro
            novo_livro = Livro(
                titulo=titulo,
                ISBN=isbn,
                ano=ano,
                editora=editora,
                quantidade=quantidade,
                Categoria=categoria
            )
            session.add(novo_livro)
            session.flush()  # Obtém o ID do novo livro

            # Associa os autores ao livro
            for id_autor in id_autores:
                associacao = AutoresDosLivros(
                    Autores_id_autor=id_autor,
                    Livros_idLivros=novo_livro.idLivros
                )
                session.add(associacao)

            # Commita a transação
            session.commit()
            return novo_livro
        except IntegrityError:
            session.rollback()
            raise
        finally:
            session.close()

    # Métodos para buscar, atualizar e deletar livros podem ser adicionados aqui.

# Exemplo de uso dos métodos:
# novo_livro = LivrosController.criar_livro('Título do Livro', 'ISBN123456', 2023, 'Editora X', 10, 'Categoria Y', [1, 2])
# livro = LivrosController.buscar_livro(1)
# atualizado = LivrosController.atualizar_livro(1, titulo='Novo Título')
# LivrosController.deletar_livro(1)