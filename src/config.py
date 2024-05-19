# src/config.py

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SCRAPING_URL = os.getenv("SCRAPING_URL", "https://www.kurzy.cz/akcie-cz/burza/")
