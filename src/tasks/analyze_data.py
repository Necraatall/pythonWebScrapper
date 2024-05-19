# src/tasks/analyze_data.py

import matplotlib.pyplot as plt
from src.db import SessionLocal
from src.models import Stock

def analyze_data():
    """Analyze the stock data and plot the results."""
    session = SessionLocal()
    stocks = session.query(Stock).all()
    
    names = [stock.name for stock in stocks]
    prices = [stock.price for stock in stocks]
    
    plt.figure(figsize=(10, 5))
    plt.plot(names, prices, marker='o')
    plt.title('Stock Prices')
    plt.xlabel('Stock Name')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    analyze_data()
