from src.models.produto import Produto

from sqlalchemy import select

def test_criar_produto(session):
    novo_produto = Produto(
       titulo = 'Produto simples',
       descricao = 'Apenas um produto simples'
    ) 

    session.add(novo_produto)
    session.commit()

    stmt = select(Produto).where(Produto.titulo == 'Produto simples')
    novo_produto_cadastrado = session.scalar(stmt)

    assert novo_produto_cadastrado.id == 1


