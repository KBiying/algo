class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp
        dp = dparray = [[0] * (n)] * (m)
        # dp func
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # init
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        # 二维动态规划怎么比案例
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # check
        print(dp)
        return dp[m - 1][n - 1]


solution_instance = Solution()
result = solution_instance.uniquePaths(3, 3)
print(result)
