# tests/test_scraper.py

import pytest
from src.scraper import fetch_data, save_data_to_db
from src.db import get_db

@pytest.fixture
def sample_data():
    return [
        {
            'name': 'Sample Stock',
            'date': '2024-05-19 00:00:00',
            'price': '100.00',
            'change': '1.00',
            'buy_price': '99.00',
            'sell_price': '101.00',
            'traded_volume': '1000',
            'price_yesterday': '99.00',
            'trade_count': '10',
            'last_change': '1.00',
            'last_trade_price': '100.00',
            'last_trade_volume': '100',
            'last_trade_time': '12:00:00'
        }
    ]

def test_fetch_data():
    data = fetch_data()
    assert len(data) > 0
    assert 'name' in data[0]

def test_save_data_to_db(db, sample_data):
    save_data_to_db(sample_data, db)
    result = db.execute("SELECT * FROM sample_stock").fetchone()
    assert result is not None
