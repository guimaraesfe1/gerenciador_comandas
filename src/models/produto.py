from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, text, Identity

from .base import Base

class Produto(Base):
    __tablename__ = 'produto'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    
    titulo: Mapped[str] = mapped_column(String(40), nullable=False, unique=True)
    descricao: Mapped[str] = mapped_column(String(200), nullable=False)
    disponivel: Mapped[bool] = mapped_column(nullable=False, server_default=text('true'))