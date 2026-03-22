from sqlalchemy.orm import declarative_base, Column, String, Integer, Boolean, float, ForeignKey
from sqlalchemy import creat_engine

# criando a conexao do db
db = creat_engine("sqlite:///banco.db")

# Cria a Base do db
Base = declarative_base()


# crinado tabelas/classes do banco
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, Primary_key=True, autoincrement=True)
    # definindo o nome da colua, tipo de dado qie ela reserva, definindo como o valor unico para cada item da tabela
    # depois falei para ele incrementear um valor automaticamente a cada novo item da Lista
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("adim", Boolean, default=False)
    # se nao for definido como TRUE, entao é falso sempre

    def __init__(self, nome, email, senha, ativo, admin):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


#Pedido
class Pedido(base):
    __tablename__ = "pedidos"
    id = Column("id", Integer, Primary_key=True, autoincrement=True)
    status = Column("status", String) # pendente, concluido ou finalizado
    usuario = Column("usuario",ForeignKey("usuarios.id"))
    preco = Column("preco", float)
    # itens = 


#


