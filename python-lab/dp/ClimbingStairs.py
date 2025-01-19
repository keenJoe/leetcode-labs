# 70. Climbing Stairs

from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        # 基本情况
        if n <= 2:
            return n
        # 递归：f(n) = f(n-1) + f(n-2)
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    

    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dp(i):
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        
        return dp(n)
    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # 初始化dp数组
        dp = [0] * (n + 1)
        dp[1] = 1  # 爬到第1阶有1种方法
        dp[2] = 2  # 爬到第2阶有2种方法
        
        # 从底向上计算
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev1 = 2  # 表示f(2)
        prev2 = 1  # 表示f(1)
        
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1