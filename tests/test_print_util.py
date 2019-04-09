import unittest

from util import printutil


class TestPrintUtil(unittest.TestCase):
    def test_print(self):
        printutil.print_key_value("Key", "Value")
