from fastapi import APIRouter, Depends
from dependencies import pegar_dependecias
from models import Usuario
auth_router = APIRouter(prefix="/auth", tags=["auth"])
@auth_router.get("/")
async def autenticar():
    return {"Mensagem": "Voce esta acessando a rota de autentificação", "autentificação": False}


@auth_router.post("/login")
async def login(email: str, senha: str, nome:str, session = Depends(pegar_dependecias)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return{"mensage": "email already exists"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem": "Sucessful Login"}
