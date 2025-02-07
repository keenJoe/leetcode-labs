# 2218. Maximum Value of K Coins From Piles

from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # dp[i][j] 表示从前i个堆中取j个硬币的最大价值
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for coins in range(k + 1):
                # 不从当前堆取硬币
                dp[i][coins] = dp[i-1][coins]
                
                # 从当前堆取硬币
                curr_sum = 0
                # 最多取min(len(piles[i-1]), coins)个硬币
                for j in range(min(len(piles[i-1]), coins)):
                    curr_sum += piles[i-1][j]
                    if coins - j - 1 >= 0:
                        dp[i][coins] = max(dp[i][coins], 
                                        dp[i-1][coins-j-1] + curr_sum)
        
        return dp[n][k]