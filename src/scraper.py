# src/scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_stock_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) >= 3:
            data.append({
                'name': columns[0].text,
                'price': float(columns[1].text),
                'change': float(columns[2].text),
            })

    return data

if __name__ == "__main__":
    data = fetch_stock_data("https://www.kurzy.cz/akcie-cz/burza/")
    print(data)