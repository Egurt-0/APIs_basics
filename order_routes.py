from fastapi import APIRouter
order_routes = APIRouter(prefix="/order", tags=["order"])

@order_routes.get("/")
async def orders():
    return {"Mensagem": "Voce acessou a rota padrao de pedidos"}

    