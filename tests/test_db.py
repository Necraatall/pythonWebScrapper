# tests/test_db.py

import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Stock

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.db_session = self.Session()

    def tearDown(self):
        self.db_session.close()

    def test_stock_model(self):
        stock = Stock(name="Test Stock", price=123.45, change=1.23)
        self.db_session.add(stock)
        self.db_session.commit()
        
        result = self.db_session.query(Stock).filter_by(name="Test Stock").first()
        self.assertEqual(result.price, 123.45)
        self.assertEqual(result.change, 1.23)

if __name__ == '__main__':
    unittest.main()
