# 509. Fibonacci Number

class Solution:
    # 递归
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
    
    # 动态规划
    def fib_1(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    # 动态规划，空间优化
    def fib_2(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev, curr = 0, 1
        for i in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(0))
    print(solution.fib(1))
    print(solution.fib(2))
    print(solution.fib(3))
    print(solution.fib(4))