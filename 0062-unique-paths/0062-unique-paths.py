class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for pos_i in range(m):
            for pos_j in range(n):
                if pos_i == 0 and pos_j == 0:
                    pass
                elif pos_i == 0:
                    dp[pos_i][pos_j] += dp[pos_i][pos_j - 1]
                elif pos_j == 0:
                    dp[pos_i][pos_j] += dp[pos_i - 1][pos_j]
                else:
                    dp[pos_i][pos_j] = dp[pos_i - 1][pos_j] + dp[pos_i][pos_j - 1]

        return dp[m - 1][n - 1]   