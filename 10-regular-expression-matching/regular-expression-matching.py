class Solution:
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        # dp[i][j] = whether s[i:] matches p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[m][n] = True

        # Fill from the end toward the beginning
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                # Does current character match?
                first_match = (
                    i < m and
                    (s[i] == p[j] or p[j] == '.')
                )

                # If the next pattern character is '*'
                if j + 1 < n and p[j + 1] == '*':
                    dp[i][j] = (
                        dp[i][j + 2] or
                        (first_match and dp[i + 1][j])
                    )

                else:
                    dp[i][j] = (
                        first_match and dp[i + 1][j + 1]
                    )

        return dp[0][0]