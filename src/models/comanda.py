from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, Identity
from datetime import datetime

from .base import Base

class Comanda(Base):
    __tablename__ = 'comanda'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    mesa_num: Mapped[int] = mapped_column(nullable=False)
    criado_em: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )

    comanda_produto = relationship('ComandaProduto', passive_deletes=True)