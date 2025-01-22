# 121. Best Time to Buy and Sell Stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')  # 记录最低价格
        max_profit = 0  # 记录最大利润
        
        for price in prices:
            # 更新最低价格
            min_price = min(min_price, price)
            # 计算当前能获得的利润
            current_profit = price - min_price
            # 更新最大利润
            max_profit = max(max_profit, current_profit)
        
        return max_profit
    

    def maxProfit(self, prices: List[int]) -> int:
        # 方法一：二维DP
        # dp[i][0] 表示第i天不持有股票的最大利润
        # dp[i][1] 表示第i天持有股票的最大利润
        if not prices:
            return 0
            
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        
        # 初始状态
        dp[0][0] = 0  # 第一天不持有
        dp[0][1] = -prices[0]  # 第一天买入
        
        # 状态转移
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  # 不持有 = max(前一天不持有，前一天持有今天卖出)
            dp[i][1] = max(dp[i-1][1], -prices[i])  # 持有 = max(前一天持有，今天买入)
            
        return dp[n-1][0]
    
    
    # 方法二：空间优化的一维DP
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        n = len(prices)
        # 初始状态
        no_stock = 0  # 不持有股票
        has_stock = -prices[0]  # 持有股票
        
        # 状态转移
        for i in range(1, n):
            no_stock = max(no_stock, has_stock + prices[i])
            has_stock = max(has_stock, -prices[i])
            
        return no_stock