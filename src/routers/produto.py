from typing import Annotated
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session
from ..database.session import get_session
from ..crud.produto import (
    atualizar_produto_service,
    deletar_produto_service,
    criar_produto_service,
    recuperar_produto_service
)
from ..schemas.produto import (
    CriarProdutoSchema,
    AtualiarProdutoSchema
)

router = APIRouter(prefix='/produto')

@router.post('', status_code=status.HTTP_201_CREATED)
def criar_produto_route(
    session: Annotated[Session, Depends(get_session)],
    produto_dados: CriarProdutoSchema
):
    criar_produto_service(session, produto_dados)
    return { 'message': 'Produto criado com sucesso!' }


@router.put('/{produto_id}', status_code=status.HTTP_200_OK)
def atualizar_produto_route(
    session: Annotated[Session, Depends(get_session)],
    produto_dados: AtualiarProdutoSchema,
    produto_id: int
):
    atualizar_produto_service(session, produto_dados, produto_id)
    return { 'message': 'Produto atualizado com sucesso!' }


@router.delete('/{produto_id}', status_code=status.HTTP_200_OK)
def deletar_produto_route(
    session: Annotated[Session, Depends(get_session)],
    produto_id: int
):
    deletar_produto_service(session, produto_id)
    return { 'message': 'Produto deletado com sucesso!' }


@router.get('/{produto_id}', status_code=status.HTTP_200_OK)
def recuperar_produto_route(
    session: Annotated[Session, Depends(get_session)],
    produto_id: int
):
    return recuperar_produto_service(session, produto_id)
