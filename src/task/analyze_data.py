# src/tasks/analyze_data.py

import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table
from ..db import get_db, engine

def plot_stock_data(stock_name: str):
    db = next(get_db())
    table_name = stock_name.lower().replace(' ', '_').replace('.', '')
    table = Table(table_name, MetaData(), autoload_with=engine)

    query = db.execute(table.select()).fetchall()
    df = pd.DataFrame(query, columns=query[0].keys())

    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['price'], label=stock_name)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'Stock Prices for {stock_name}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    stock_name = 'Example Stock Name'  # Replace with actual stock name
    plot_stock_data(stock_name)
