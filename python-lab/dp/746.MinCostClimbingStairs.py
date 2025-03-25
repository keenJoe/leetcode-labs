# 746. Min Cost Climbing Stairs

"""
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

示例 1：

输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。

示例 2：

输入：cost = [1,100,1,1,1,100,1,1,100,1]
输出：6
解释：你将从下标为 0 的台阶开始。

dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]
    
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev2, prev1 = 0, 0  # dp[0], dp[1]
        
        for i in range(2, n + 1):
            current = min(prev1 + cost[i-1], 
                        prev2 + cost[i-2])
            prev2, prev1 = prev1, current
        
        return prev1
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostClimbingStairs([10, 15, 20]))
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
