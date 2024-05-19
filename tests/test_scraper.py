# tests/test_scraper.py

import unittest
from src.scraper import fetch_stock_data

class TestScraper(unittest.TestCase):

    def test_fetch_stock_data(self):
        url = "https://www.kurzy.cz/akcie-cz/burza/"
        data = fetch_stock_data(url)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        for item in data:
            self.assertIn('name', item)
            self.assertIn('price', item)
            self.assertIn('change', item)

if __name__ == '__main__':
    unittest.main()
