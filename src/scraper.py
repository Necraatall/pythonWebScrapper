# src/scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_stock_data(url):
    # Request the webpage
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data from {url}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing stock data
    table = soup.find('table', class_='your-table-class')  # Adjust 'your-table-class' accordingly

    # Extract stock data from the table
    stock_data = []
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) >= 13:  # Assuming there are 13 columns
                # Extract data from columns and create a dictionary for each stock
                stock = {
                    'name': columns[0].text.strip(),
                    'price': columns[1].text.strip(),
                    'change': columns[2].text.strip(),
                    'buy_price': columns[3].text.strip(),
                    'sell_price': columns[4].text.strip(),
                    'traded_volume': columns[5].text.strip(),
                    'price_yesterday': columns[6].text.strip(),
                    'trade_count': columns[7].text.strip(),
                    'last_change': columns[8].text.strip(),
                    'last_trade_price': columns[9].text.strip(),
                    'last_trade_volume': columns[10].text.strip(),
                    'last_trade_time': columns[11].text.strip(),
                    'ks': columns[12].text.strip()
                }
                stock_data.append(stock)

    return stock_data
