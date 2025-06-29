# 69. Sqrt(x)

"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # 返回right，因为要向下取整


if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(4))
    print(solution.mySqrt(8))
    print(solution.mySqrt(16))
    print(solution.mySqrt(25))
    print(solution.mySqrt(36))
    print(solution.mySqrt(49))
    print(solution.mySqrt(64))