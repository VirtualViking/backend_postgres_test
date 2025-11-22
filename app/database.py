import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- CONFIGURACIÓN POSTGRESQL ---
# GitHub Actions usará estas variables.
# Tu PC usará los valores por defecto (postgres/5432).

db_user = os.getenv("POSTGRES_USER", "postgres")
# OJO: Cambia "tu_password_local" por la clave que pusiste al instalar Postgres en tu PC
db_password = os.getenv("POSTGRES_PASSWORD", "root") 
db_host = os.getenv("POSTGRES_HOST", "localhost")
db_port = os.getenv("POSTGRES_PORT", "5432")
db_name = os.getenv("POSTGRES_DB", "parcial_db")

# Driver postgresql
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()