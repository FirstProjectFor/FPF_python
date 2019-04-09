import unittest

from util import print_util


class TestPrintUtil(unittest.TestCase):
    def test_print(self):
        print_util.print_key_value("Key", "Value")
