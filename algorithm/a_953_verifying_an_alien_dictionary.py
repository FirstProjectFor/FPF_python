class Solution:
    def isAlienSorted(self, words, order):
        m = {o: i for i, o in enumerate(order)}
        words = [[m[w] for w in word] for word in words]

        for w1, w2 in zip(words, words[1:]):
            if w1 > w2:
                return False

        return True


solution = Solution()
print(solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
print(solution.isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz"))
