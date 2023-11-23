import logging


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 5mins 没有思路

        # dp array
        dp = [0] * (n + 1)
        # dp function

        # dp init
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n + 1):
            print("i = {}".format(i))
            for j in range(1, i + 1):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
                print(
                    "j = {}, (i-j) = {},  j * (i - j) = {}, j * dp[i - j] = {}".format(
                        j, (i - j), j * (i - j), j * dp[i - j]
                    )
                )
                print(dp)
        # check
        # print(dp)
        return dp[n]


myinstan = Solution()
result = myinstan.integerBreak(4)
print(result)
