class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> list:

        word_dict = {}
        result = []

        words = A.split() + B.split()

        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        for k, v in word_dict.items():
            if v == 1:
                result.append(k)

        return result


solution = Solution()
print(solution.uncommonFromSentences("this apple  is sweet", "this apple is sour"))
