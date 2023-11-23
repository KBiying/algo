class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 没思路，我忘记二叉搜索树是什么：左小右大于根
        # dp array
        dp = [0] * (n + 1)

        # dp init
        dp[0] = 1
        dp[1] = 1
        # dp func
        for i in range(2, n + 1):
            for j in range(1, n + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        # check
        return dp[n]
