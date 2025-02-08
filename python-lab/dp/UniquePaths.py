# 62. Unique Paths

'''
    方案一：使用递归
        1、递归的终止条件：当到达终点时，返回1。
        2、递归的参数：当前位置的坐标(x, y)
            1、需要判断是否越界，x >= m or y >= n，此时返回0；
            2、需要判断是否到达终点，x == m - 1 and y == n - 1，此时事到达终点，返回1；
            4、其他情况，返回从当前位置向右走一步，再向下走一步，然后递归计算从当前位置到终点的路径数；
        3、递归的返回值：从当前位置到终点的路径数
        4、递归的逻辑：从当前位置向右走一步，再向下走一步，然后递归计算从当前位置到终点的路径数
    方案二：使用动态规划
        1、动态规划的初始化：创建一个二维数组dp，dp[i][j]表示从起点到(i, j)的路径数
        2、动态规划的转移方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        3、动态规划的初始化：dp[0][0] = 1
        4、动态规划的返回值：dp[m-1][n-1]
'''

class Solution:
    # 使用递归
    def uniquePaths(self, m: int, n: int) -> int:
        cach = {}
        
        def uniquePaths_recursion(x: int, y: int) -> int:
            if (x, y) in cach:
                return cach[(x, y)]
            # 判断是否越界
            if x >= m or y >= n:
                return 0
            # 判断是否到达终点
            if x == m - 1 and y == n - 1:
                return 1
            cach[(x, y)] = uniquePaths_recursion(x + 1, y) + uniquePaths_recursion(x, y + 1)
            return cach[(x, y)]
        
        return uniquePaths_recursion(0, 0)
    
    # 使用动态规划
    # 时间复杂度：O(m * n)
    # 从递归的思路中，可以发现，递归的思路是从终点向起点推导，而动态规划的思路是从起点向终点推导。
    # 如果既可以使用动态规划，也可以使用递归，那么通常能够从递归推倒出动态规划的解法。
    def uniquePaths_1(self, m: int, n: int) -> int:
        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

if __name__ == "__main__":
    m = 3
    n = 7
    print(Solution().uniquePaths_1(m, n))
