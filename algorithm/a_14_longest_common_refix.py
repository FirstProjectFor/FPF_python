class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs:
            return ""

        result = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]

        for ch1, ch2 in zip(last, first):
            if ch1 == ch2:
                result += ch1
            else:
                break

        return result


solution = Solution()

print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
print(solution.longestCommonPrefix([]))
