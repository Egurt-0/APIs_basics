from pydantic import BaseModel, ConfigDict
from typing import Optional      



class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha:  str
    ativo: Optional[bool] = None
    admin: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)  # permite criar o modelo a partir de objetos ORM (ex: SQLAlchemy)