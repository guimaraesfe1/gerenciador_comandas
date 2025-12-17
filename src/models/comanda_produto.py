from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, CheckConstraint

from .base import Base

class ComandaProduto(Base):
    __tablename__ = 'comanda_produto'
    
    id_comanda: Mapped[int] = mapped_column(
        ForeignKey('comanda.id', ondelete='CASCADE'), primary_key=True
    )
    id_produto: Mapped[int] = mapped_column(
        ForeignKey('produto.id'), primary_key=True
    )
    quantidade: Mapped[int] = mapped_column(nullable=False)

    __table_args__ = (
        CheckConstraint('quantidade > 0', name='ck_quantidade_positive'),
    )