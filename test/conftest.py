import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    
    from src.models.base import Base
    import src.models

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    Base.metadata.drop_all(engine)
    engine.dispose()w
