# src/scraper.py

import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def fetch_stock_data(url: str) -> List[Dict[str, str]]:
    """Fetches stock data from the given URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    stocks = []
    for row in soup.select('table tbody tr'):
        stock = {
            'name': row.select_one('td.name').text,
            'price': row.select_one('td.price').text,
            'change': row.select_one('td.change').text,
        }
        stocks.append(stock)
    return stocks

if __name__ == "__main__":
    data = fetch_stock_data("https://www.kurzy.cz/akcie-cz/burza/")
    print(data)
