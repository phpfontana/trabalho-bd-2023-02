from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import Session
from models import Base
from sqlalchemy.ext.declarative import declarative_base

class emprestimo_controller:

    def __init__(self, session: Session):
        self.session = session

    def cadastrar_emprestimo (self, livro_id):
    
        Livro = self.session.query(Livro).filter_by(idLivro=livro_id).first()
        if (livro.cadastrado == True):

            print('Livro ja se encontra emprestado')

        else:
            livro.cadastrado == True
            print('Emprestimo cadastrado com sucesso')

