class A_516:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0

        length = len(s)
        dp = [[0] * length for i in range(length)]
        for index in range(length):
            dp[index][index] = 1

        for l in range(2, length + 1):
            for end in range(l - 1, length, 1):
                start = end - l + 1
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1] + 2
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
        return dp[0][length - 1]
