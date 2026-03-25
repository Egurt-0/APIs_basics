from fastapi import APIRouter, Depends, HTTPException
from dependencies import pegar_dependecias
from models import Usuario
from main import bcrypts_context
from schemas import UsuarioSchema




auth_router = APIRouter(prefix="/auth", tags=["auth"])
@auth_router.get("/")
async def autenticar():
    return {"Mensagem": "Voce esta acessando a rota de autentificação", "autentificação": False}


@auth_router.post("/login")
async def login(usuario_schemas: UsuarioSchema, session = Depends(pegar_dependecias)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schemas.email).first()
    if usuario:
        raise  HTTPException(status_code=400, detail="Este email ja esta sendo usado")
    else:
        senha_criptografada = bcrypts_context.hash(usuario_schemas.senha) # transformando a senha em hash
        novo_usuario = Usuario(usuario_schemas.nome, usuario_schemas.email, senha_criptografada, usuario_schemas.ativo, usuario_schemas.admin)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem": f"Sucessful Login, Welcome {novo_usuario}"}