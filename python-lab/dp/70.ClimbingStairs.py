# 70. Climbing Stairs

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

提示：

1 <= n <= 45

当n=1时，有1种方法爬到楼顶
当n=2时，有2种方法，分别是1+1和2
当n=3时，有3种方法，分别是1+1+1、1+2和2+1
当n=4时，有5种方法，分别是(n=3)+1、1+(n=3)、(n=3)+1、(n=3)+1和2+2
    当n=3时，走向n=4的方法有2种，分别是(n=3)+1和1+(n=3)
    当n=2时，走向n=4的方法有3种，分别是(n=2)+2、2+(n=2)和(n=2)+1+(n=2)
    当n=1时，走向n=4的方法有5种，分别是(n=1)+3、1+(n=3)、(n=1)+2+1、1+(n=2)+1和1+1+(n=2)
    
    由此可以推断，走向n的方法数为走向n-1的方法数和走向n-2的方法数之和
'''

from typing import List

class Solution:
    # 递归
    def climbStairs(self, n: int) -> int:
        # 基本情况
        if n <= 2:
            return n
        # 递归：f(n) = f(n-1) + f(n-2)
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    # 记忆化搜索
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
    
    # 动态规划，自顶向下
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
    
    # 动态规划，自底向上，优化空间复杂度
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