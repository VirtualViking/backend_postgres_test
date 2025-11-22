import pytest
from sqlalchemy import text
from app.database import engine
from fastapi.testclient import TestClient
from app.main import app

# FIXTURE: Configuración para limpiar la BD antes de cada prueba (Versión PostgreSQL)

@pytest.fixture(scope="function", autouse=True)
def clean_db():
    """Limpia las tablas antes de cada prueba para empezar de cero."""
    with engine.connect() as connection:
        try:
            transaction = connection.begin()
            
            # COMANDO CORREGIDO PARA POSTGRES:
            # MySQL usaba: SET FOREIGN_KEY_CHECKS = 0
            # Postgres usa: TRUNCATE ... CASCADE
            connection.execute(text("TRUNCATE TABLE tasks, users RESTART IDENTITY CASCADE"))
            
            transaction.commit()
        except Exception as e:
            transaction.rollback()
            raise e

@pytest.fixture(scope="module")
def client():
    """Entrega el cliente de pruebas para hacer peticiones."""
    return TestClient(app)