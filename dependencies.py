from models import db
from sqlalchemy.orm import sessionmaker

def pegar_dependecias():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally: # executa independente do resultado do try
        session.close() # necessario fechar a sessao para nao dar merda e ficar com um monte de sessao aberta