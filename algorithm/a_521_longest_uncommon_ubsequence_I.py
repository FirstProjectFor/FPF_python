class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        result = -1
        if len(a) != len(b):
            result = max(len(a), len(b))
        elif a.find(b) == -1:
            result = len(a)
        elif b.find(a) == -1:
            result = len(b)
        return result


solution = Solution()
print(solution.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))
