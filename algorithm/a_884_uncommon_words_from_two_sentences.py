class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> list:

        word_dict_a = {}
        word_dict_b = {}
        result = []

        for word in A.split():
            if word in word_dict_a:
                word_dict_a[word] += 1
            else:
                word_dict_a[word] = 1

        for word in B.split():
            if word in word_dict_b:
                word_dict_b[word] += 1
            else:
                word_dict_b[word] = 1

        for word in A.split():
            if word_dict_a[word] == 1 and word not in word_dict_b:
                result.append(word)

        for word in B.split():
            if word_dict_b[word] == 1 and word not in word_dict_a:
                result.append(word)

        return result


solution = Solution()
print(solution.uncommonFromSentences("this apple  is sweet", "this apple is sour"))
