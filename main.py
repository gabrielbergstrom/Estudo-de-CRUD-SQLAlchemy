from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo

class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtd_paginas = Column("qtd_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))
    
    def __init__(self, titulo, qtd_paginas, dono,):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas
        self.dono = dono

Base.metadata.create_all(bind=db)

#CRUD


#Create

# usuario = Usuario(nome="gabriel", email="gbr@gmail.com", senha="123")
# session.add(usuario)
# session.commit()

# usuario = Usuario(nome="gabriel2", email="gbr2@gmail.com", senha="123")
# session.add(usuario)
# session.commit()

#Read

# lista_usuarios = session.query(Usuario).all()
# usuario_gbr = session.query(Usuario).filter_by(email="gbr@gmail.com").first()
# print(usuario_gbr)
# print(usuario_gbr.nome)
# print(usuario_gbr.email)

# usuario_gbr2 = session.query(Usuario).filter_by(email="gbr2@gmail.com").first()
# print(usuario_gbr2)
# print(usuario_gbr2.nome)
# print(usuario_gbr2.email)


# livro = Livro(titulo="Programador Pragmatico", qtd_paginas=300, dono=usuario_gbr.id)
# session.add(livro)
# session.commit()

#Update

# usuario_gbr.nome = "gabrielbergstrom"
# session.add(usuario_gbr)
# session.commit()

#Delete

# session.delete(usuario_gbr2)
# session.commit()
