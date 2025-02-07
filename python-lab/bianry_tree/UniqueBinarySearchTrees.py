# 96. Unique Binary Search Trees

from typing import List

class Solution:
    # 1. 动态规划，使用一个数组来存储每个节点作为根节点时，二叉搜索树的数量。
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]
    
    # 2. 记忆化递归，使用一个字典来存储每个节点作为根节点时，二叉搜索树的数量。
    def __init__(self):
        self.memo = {}
    
    def numTrees(self, n: int) -> int:
        # base case
        if n <= 1:
            return 1
            
        # 记忆化查询
        if n in self.memo:
            return self.memo[n]
            
        count = 0
        for i in range(1, n + 1):
            left = self.numTrees(i - 1)    # 左子树的可能数量
            right = self.numTrees(n - i)    # 右子树的可能数量
            count += left * right           # 状态转移方程
            
        # 存入记忆化字典
        self.memo[n] = count
        return count