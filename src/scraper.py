# src/scraper.py

import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from sqlalchemy.orm import Session
from datetime import datetime
from .db import get_db, engine
from .models import create_stock_table

BASE_URL = "https://www.kurzy.cz/akcie-cz/burza/"

def fetch_data() -> List[Dict]:
    response = requests.get(BASE_URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'stockTable'})

    data = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) < 12:
            continue
        stock_data = {
            'name': cols[0].get_text(strip=True),
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'price': cols[1].get_text(strip=True),
            'change': cols[2].get_text(strip=True),
            'buy_price': cols[3].get_text(strip=True),
            'sell_price': cols[4].get_text(strip=True),
            'traded_volume': cols[5].get_text(strip=True),
            'price_yesterday': cols[6].get_text(strip=True),
            'trade_count': cols[7].get_text(strip=True),
            'last_change': cols[8].get_text(strip=True),
            'last_trade_price': cols[9].get_text(strip=True),
            'last_trade_volume': cols[10].get_text(strip=True),
            'last_trade_time': cols[11].get_text(strip=True)
        }
        data.append(stock_data)

    return data

def save_data_to_db(data: List[Dict], db: Session):
    for stock in data:
        table = create_stock_table(stock['name'])
        table.create(engine, checkfirst=True)
        insert_stmt = table.insert().values(
            date=stock['date'],
            price=stock['price'],
            change=stock['change'],
            buy_price=stock['buy_price'],
            sell_price=stock['sell_price'],
            traded_volume=stock['traded_volume'],
            price_yesterday=stock['price_yesterday'],
            trade_count=stock['trade_count'],
            last_change=stock['last_change'],
            last_trade_price=stock['last_trade_price'],
            last_trade_volume=stock['last_trade_volume'],
            last_trade_time=stock['last_trade_time']
        )
        db.execute(insert_stmt)
    db.commit()

def main():
    db = next(get_db())
    data = fetch_data()
    save_data_to_db(data, db)

if __name__ == "__main__":
    main()
