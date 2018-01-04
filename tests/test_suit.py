import unittest

from tests.test_demo import TestDemo

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDemo))

    try:
        with open("test.txt", mode="w", encoding="utf-8") as t:
            runner = unittest.TextTestRunner(stream=t, verbosity=2)
            runner.run(suite)
    except FileNotFoundError as e:
        print("测试出错", str(e))
