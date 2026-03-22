from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType
# criando a conexao do db
db = create_engine("sqlite:///banco.db")

# Cria a Base do db
Base = declarative_base()


# crinado tabelas/classes do banco
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    # definindo o nome da colua, tipo de dado qie ela reserva, definindo como o valor unico para cada item da tabela
    # depois falei para ele incrementear um valor automaticamente a cada novo item da Lista
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)
    # se nao for definido, entao é falso sempre

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


#Pedido
class Pedido(Base):
    __tablename__ = "pedidos"
#    STATUS_PEDIDOS = (
#        ("PENDENTE", "PENDENTE"),
#        ("CANCELADO", "CANCELADO"),
#        ("FINALIZADO", "FINALIZADO")
#
#    )
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # pendente, Cancelado ou finalizado
    usuario = Column(Integer, ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    # itens = 

    def __init__(self, id,usuario,status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status

#ItensPedidos
class ItensPedidos(Base):
    __tablename__ = "itens_pedido"
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", Integer)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column(Integer, ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho  
        self.preco_unitario = preco_unitario
        self.pedido = pedido


