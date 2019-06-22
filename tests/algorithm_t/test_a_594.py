from unittest import TestCase
from algorithm.a_594_longest_harmonious_subsequence import Algorithm


class A_594_Test(TestCase):
    def setUp(self):
        self.algorithm = Algorithm()
        super().setUp()

    def testLongestPalindromeSubSeq(self):
        self.assertEqual(0, self.algorithm.findLHS(None))
        self.assertEqual(0, self.algorithm.findLHS([]))

        self.assertEqual(0, self.algorithm.findLHS([1]))
        self.assertEqual(0, self.algorithm.findLHS([1, 1, 1]))

        self.assertEqual(2, self.algorithm.findLHS([1, 2, 3, 4, 5, 6, 7, 8, 9]))
