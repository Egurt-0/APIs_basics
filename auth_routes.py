from fastapi import APIRouter, Depends
from dependencies import pegar_dependecias
from models import Usuario
from main import bcrypts_context
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
        senha_criptografada = bcrypts_context.hash(senha[:72]) # transformando a senha em hash
        novo_usuario = Usuario(nome, email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem": "Sucessful Login"}