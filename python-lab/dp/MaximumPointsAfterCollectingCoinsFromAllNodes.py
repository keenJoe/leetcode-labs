# 2920. Maximum Points After Collecting Coins From All Nodes

from typing import List

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        # dp[i][j] 表示从节点i开始，收集j个硬币的最大价值
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = coins[i]
        
        for i in range(n):
            for j in range(1, k + 1):
                dp[i][j] = dp[i][j-1] + coins[i]
        
        return dp[0][k]