class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not str:
            return False

        length = len(s)
        rev = s[-1:-length - 1:-1]
        if s == rev:
            return True
        else:
            for index in range(length):
                if s[index] != rev[index]:
                    s = s[0:index:1] + s[index + 1:length:1]
                    rev = rev[0:index:1] + rev[index + 1:length:1]
                    return s == s[-1:-length - 1:-1] or rev == rev[-1:-length - 1:-1]


solution = Solution()
print(solution.validPalindrome("q"))
print(solution.validPalindrome("aba"))
print(solution.validPalindrome("avbba"))
print(solution.validPalindrome("abca"))
print(solution.validPalindrome("abcca"))
print(solution.validPalindrome("abc"))
print(solution.validPalindrome("abcvcba"))
print(solution.validPalindrome("avvca"))
print(solution.validPalindrome("avcvca"))
print(solution.validPalindrome("aaaaccccaaa"))
print(solution.validPalindrome(
    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
