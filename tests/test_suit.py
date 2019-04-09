import unittest

from tests.test_demo import TestDemo
from tests.test_string import TestStringMethods
from tests.test_print_util import TestPrintUtil

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDemo))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestStringMethods))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPrintUtil))

    try:
        with open("test.txt", mode="w", encoding="utf-8") as t:
            runner = unittest.TextTestRunner(stream=t, verbosity=2)
            runner.run(suite)
    except FileNotFoundError as e:
        print("测试出错", str(e))
