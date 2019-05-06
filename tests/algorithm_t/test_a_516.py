from unittest import TestCase
from algorithm.a_516_longest_palindromic_subsequence import A_516


class A_516_Test(TestCase):
    def setUp(self):
        self.a_516 = A_516()
        super().setUp()

    def testLongestPalindromeSubSeq(self):
        self.assertEqual(0, self.a_516.longestPalindromeSubseq(s=''))
        self.assertEqual(1, self.a_516.longestPalindromeSubseq(s='a'))
        self.assertEqual(1, self.a_516.longestPalindromeSubseq(s='ab'))
        self.assertEqual(2, self.a_516.longestPalindromeSubseq(s='aa'))
        self.assertEqual(3, self.a_516.longestPalindromeSubseq(s='aca'))
        self.assertEqual(3, self.a_516.longestPalindromeSubseq(s='caca'))
        self.assertEqual(4, self.a_516.longestPalindromeSubseq(s='bbbab'))
        self.assertEqual(5, self.a_516.longestPalindromeSubseq(s='abcdefghijdasd'))
