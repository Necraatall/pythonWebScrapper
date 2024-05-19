# src/tasks/fetch_data.py

from src.scraper import fetch_stock_data
from src.db import SessionLocal
from src.models import Stock
from src.config import SCRAPING_URL
from datetime import datetime

def save_data_to_db(data):
    """Saves the fetched data to the database."""
    session = SessionLocal()
    for item in data:
        stock = Stock(
            name=item['name'],
            price=float(item['price'].replace(',', '.')),
            change=float(item['change'].replace(',', '.')),
            timestamp=datetime.now()
        )
        session.add(stock)
    session.commit()
    session.close()

def main():
    """Main function to fetch and save data."""
    data = fetch_stock_data(SCRAPING_URL)
    save_data_to_db(data)

if __name__ == "__main__":
    main()
