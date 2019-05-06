import unittest

from tests.test_demo import TestDemo
from tests.test_print_util import TestPrintUtil
from tests.test_string import TestStringMethods
from tests.test_time_record import TestTimeRecord
from tests.algorithm_t.test_a_829 import A_829
from tests.algorithm_t.test_a_516 import A_516_Test

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDemo))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestStringMethods))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPrintUtil))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTimeRecord))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(A_829))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(A_516_Test))

    try:
        with open("test.txt", mode="w", encoding="utf-8") as t:
            runner = unittest.TextTestRunner(stream=t, verbosity=2)
            runner.run(suite)
    except FileNotFoundError as e:
        print("测试出错", str(e))
