from sqlalchemy import Table, Column, String, Integer, MetaData
from .db import metadata, engine

def create_stock_table(stock_name: str):
    table_name = stock_name.lower().replace(' ', '_').replace('.', '')
    return Table(
        table_name,
        metadata,
        Column('id', Integer, primary_key=True, index=True),
        Column('date', String, nullable=False),
        Column('price', String),
        Column('change', String),
        Column('buy_price', String),
        Column('sell_price', String),
        Column('traded_volume', String),
        Column('price_yesterday', String),
        Column('trade_count', String),
        Column('last_change', String),
        Column('last_trade_price', String),
        Column('last_trade_volume', String),
        Column('last_trade_time', String),
        extend_existing=True
    )

def get_or_create_stock_table(name: str):
    table = create_stock_table(name)
    if not engine.dialect.has_table(engine, table.name):
        metadata.create_all(bind=engine)
    return table
