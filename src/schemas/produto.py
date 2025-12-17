from pydantic import BaseModel, Field
from typing import Optional


class CriarProdutoSchema(BaseModel):
    titulo: str = Field(max_length=40)
    descricao: str = Field(max_length=200)
    disponivel: Optional[bool] = True

class AtualiarProdutoSchema(BaseModel):
    titulo: Optional[str] = Field(max_length=40)
    descricao: Optional[str] = Field(max_length=200)
    disponivel: Optional[bool]