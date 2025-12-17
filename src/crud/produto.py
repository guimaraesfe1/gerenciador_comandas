from sqlalchemy.orm import Session
from ..schemas.produto import (
    CriarProdutoSchema,
    AtualiarProdutoSchema,
)
from sqlalchemy.exc import IntegrityError
from ..models.produto import Produto
from ..exceptions.produto import (
    ProdutoJaExisteException,
    ProdutoNaoEncontradoException
)

def criar_produto_service(session: Session,
                          produto_dados: CriarProdutoSchema
) -> None:
    produto_dados_dict = produto_dados.model_dump(exclude_none=True)

    novo_produto = Produto(**produto_dados_dict)

    try:
        session.add(novo_produto)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise ProdutoJaExisteException

def atualizar_produto_service(session: Session,
                              produto_dados: AtualiarProdutoSchema,
                              produto_id: int
) -> Produto:
    get_produto = session.get(Produto, produto_id)

    if not get_produto:
        raise ProdutoNaoEncontradoException

    produto_dados_dict = produto_dados.model_dump(exclude_none=True)
    
    for campo, valor in produto_dados_dict.items():
        setattr(get_produto, campo, valor)

    session.commit()
    session.refresh(get_produto)

    return get_produto
    

def recuperar_produto_service(session: Session,
                              produto_id: int
) -> Produto:
    get_produto = session.get(Produto, produto_id)

    if not get_produto:
        raise ProdutoNaoEncontradoException
    
    return get_produto

def deletar_produto_service(session: Session,
                            produto_id: int
) -> None:
    get_produto = session.get(Produto, produto_id)

    if not get_produto:
        raise ProdutoNaoEncontradoException

    session.delete(get_produto)
    session.commit()