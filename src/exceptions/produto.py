from fastapi import HTTPException, status

ProdutoNaoEncontradoException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Produto não encontrado!'
)

ProdutoJaExisteException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Produto já existe'
)