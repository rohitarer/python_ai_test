import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from database import Base, get_db

@pytest.fixture
def client(tmp_path):

    test_engine = create_engine(
        f"sqlite:///{tmp_path / 'test_tickets.db'}",
        connect_args= {"check_same_thread": False}
    )

    TestingSessionLocal = sessionmaker(bind= test_engine)

    Base.metadata.create_all(bind= test_engine)

    def override_get_db():
        db = TestingSessionLocal()

        try:
            yield db
        finally:
            db.close()


    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as testclient:
        yield testclient

    app.dependency_overrides.clear()
    test_engine.dispose()


def test_get_empty_tickets(client):
    response = client.get("/tickets")

    assert response.status_code == 200
    assert response.json() == []