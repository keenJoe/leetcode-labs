# 1025. Divisor Game

"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 n 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < n 且 n % x == 0 。
用 n - x 替换黑板上的数字 n 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 true 。假设两个玩家都以最佳状态参与游戏。

 

示例 1：

输入：n = 2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：n = 3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。




"""

from functools import lru_cache

class Solution:
    # 方法1：数学解法（最优）
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
    
    # 方法2：记忆化递归（用于理解过程）
    def divisorGame2(self, n: int) -> bool:
        @lru_cache(None)
        def can_win(n: int) -> bool:
            if n == 1:
                return False
            
            # 只需要检查最小的因数
            for x in range(1, int(n**0.5) + 1):
                if n % x == 0 and not can_win(n - x):
                    return True
            return False
        
        return can_win(n)
    
    # 方法3：动态规划（教学用）
    def divisorGame3(self, n: int) -> bool:
        if n == 1:
            return False
            
        dp = [False] * (n + 1)
        dp[2] = True
        
        for i in range(3, n + 1):
            # 只需要检查小的因数
            for x in range(1, i//2 + 1):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
        
        return dp[n]

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 测试不同的n值
    test_cases = [1, 2, 3, 4, 5, 6, 7, 8]
    
    print("测试结果：")
    for n in test_cases:
        result = solution.divisorGame(n)
        print(f"n = {n}: {'爱丽丝赢' if result else '鲍勃赢'}")
