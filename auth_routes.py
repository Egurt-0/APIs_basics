from fastapi import APIRouter
auth_router = APIRouter(prefix="/auth", tags=["auth"])
@auth_router.get("/")
async def autenticar():
    return {"Mensagem": "Voce esta acessando a rota de autentificação", "autentificação": False}