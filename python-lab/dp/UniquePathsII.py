# 63. Unique Paths II

'''
    这道题和Unique Paths非常相似，唯一的区别是，这道题中，网格中可能存在障碍物。
    障碍物用1表示，空地用0表示。
    机器人从左上角出发，只能向下或向右移动，不能向上或向左移动。
    问机器人从左上角到右下角有多少条不同的路径。
'''

from typing import List


class Solution:
    # 使用递归
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        
        def uniquePathsWithObstacles_recursion(x: int, y: int) -> int:
            if x == m - 1 and y == n - 1:
                return 1
            if x >= m or y >= n or obstacleGrid[x][y] == 1:
                return 0
            return uniquePathsWithObstacles_recursion(x + 1, y) + uniquePathsWithObstacles_recursion(x, y + 1)
        return uniquePathsWithObstacles_recursion(0, 0)
    
    # 使用动态规划
    def uniquePathsWithObstacles_1(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp[m - 1][n - 1]
    
    
    def uniquePathsWithObstacles_2(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        dp = [0] * n
        dp[0] = 1
        
        # 初始化第一行
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                dp[j] = 0
            else:
                dp[j] = dp[j-1]
        
        # 逐行更新
        for i in range(1, m):
            # 如果当前行的第一个位置有障碍，则设为0
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    # dp[j]代表上方的值，dp[j-1]代表左方的值
                    dp[j] = dp[j] + dp[j-1]
                
        return dp[n-1]
    
    
    
if __name__ == "__main__":
    obstacleGrid = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
    print(Solution().uniquePathsWithObstacles_1(obstacleGrid))
    print(Solution().uniquePathsWithObstacles_2(obstacleGrid))