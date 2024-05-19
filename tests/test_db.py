# tests/test_db.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db import metadata, get_db

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    metadata.drop_all(bind=engine)

def test_create_table(db):
    from src.models import create_stock_table
    table = create_stock_table("Test Stock")
    table.create(engine, checkfirst=True)
    assert table.exists(engine)
