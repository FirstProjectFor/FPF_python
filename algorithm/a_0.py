class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern or not str:
            return False

        result_dict = {}
        result_dict_reverse = {}
        words = str.split(' ')
        if len(pattern) != len(words):
            return False

        for k, v in zip(pattern, str.split(' ')):
            if result_dict.get(k) and result_dict[k] != v:
                return False
            if result_dict_reverse.get(v) and result_dict_reverse[v] != k:
                return False
            result_dict[k] = v
            result_dict_reverse[v] = k

        return True


s = Solution()

print(s.wordPattern("aa", "aa aa"))
print(s.wordPattern("abba", "dog dog dog dog"))
print(s.wordPattern("aab", "dog dog dog"))
print(s.wordPattern("aaa", "aa aa aa aa"))
