
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            left = 0

            for j in range(n):
                if grid[i][j] == 1:
                    # Mirror: swap the incoming directions
                    left, dp[j] = dp[j], left
                else:
                    # Empty cell: both directions can continue
                    left = (left + dp[j]) % MOD
                    dp[j] = left

        return left
