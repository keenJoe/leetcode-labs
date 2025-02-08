# 2920. Maximum Points After Collecting Coins From All Nodes

from typing import List

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        # 建图
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # 添加记忆化数组
        # memo[node][div] 记录从node节点开始、硬币除以2的次数为div时的最大得分
        memo = [[-1] * 14 for _ in range(n)]
        
        def dfs(node: int, parent: int, div: int) -> int:
            if div >= 14:
                return 0
            
            # 如果已经计算过，直接返回记忆化的结果
            if memo[node][div] != -1:
                return memo[node][div]
                
            coin = coins[node] >> div
            
            # 选择1：减去k
            val1 = coin - k
            # 选择2：除以2
            val2 = coin >> 1
            
            sum1 = sum2 = 0
            for next_node in graph[node]:
                if next_node != parent:
                    child = dfs(next_node, node, div)
                    child2 = dfs(next_node, node, div + 1)
                    sum1 += child
                    sum2 += child2
            
            # 存储并返回最优结果
            memo[node][div] = max(val1 + sum1, val2 + sum2)
            return memo[node][div]
        
        return dfs(0, -1, 0)