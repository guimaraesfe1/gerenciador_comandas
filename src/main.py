from fastapi import FastAPI

from .routers import (
    produto
)

app = FastAPI(
    title='Gerenciador de Comandas',
    version='1.0.0'
)

app.include_router(produto.router)