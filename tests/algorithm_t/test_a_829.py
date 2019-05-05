from unittest import TestCase

from algorithm.a_829_consecutive_numbers_sum import A_829


class A829Test(TestCase):
    def setUp(self):
        self.solution = A_829()

    def tearDown(self):
        super().tearDown()

    def test_getSum(self):
        self.assertEqual(1, A_829.get_sum(1, 1))
        self.assertEqual(6, A_829.get_sum(1, 3))
        self.assertEqual(10, A_829.get_sum(1, 4))
        self.assertEqual(5050, A_829.get_sum(1, 100))
        self.assertEqual(50005000, A_829.get_sum(1, 10000))
        self.assertEqual(1250025000, A_829.get_sum(1, 50000))
        self.assertEqual(5000050000, A_829.get_sum(1, 100000))

    def test_consecutiveNumbersSum(self):
        self.assertEqual(1, self.solution.consecutiveNumbersSum(1))
        self.assertEqual(1, self.solution.consecutiveNumbersSum(2))
        self.assertEqual(2, self.solution.consecutiveNumbersSum(3))
        self.assertEqual(1, self.solution.consecutiveNumbersSum(4))
        self.assertEqual(2, self.solution.consecutiveNumbersSum(5))
        self.assertEqual(3, self.solution.consecutiveNumbersSum(9))
        self.assertEqual(4, self.solution.consecutiveNumbersSum(15))
        self.assertEqual(5, self.solution.consecutiveNumbersSum(10000))
        self.assertEqual(10, self.solution.consecutiveNumbersSum(1000000000))
