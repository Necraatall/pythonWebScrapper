# tests/test_utils.py

import unittest
import logging
from src.utils import setup_logger

class TestUtils(unittest.TestCase):

    def test_setup_logger(self):
        logger = setup_logger("test_logger")
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.name, "test_logger")

if __name__ == '__main__':
    unittest.main()
