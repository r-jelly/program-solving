class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * 1001
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n+1):
            dp[i] = (dp[i-1]*2 + dp[i-3]) % 1000000007

        return dp[n]
