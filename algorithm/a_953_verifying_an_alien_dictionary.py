class Solution:
    def isAlienSorted(self, words, order):
        order_dict = {}
        for index, o_c in enumerate(order):
            order_dict[o_c] = index + 1

        words = [[order_dict[w] for w in word] for word in words]
        return all(w2 > w1 for w1, w2 in zip(words, words[1:]))


solution = Solution()
print(solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
print(solution.isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz"))
