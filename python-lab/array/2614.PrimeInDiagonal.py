# 2614. Prime In Diagonal

"""
    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15 16
    
    先确认对角线上的元素是哪些，然后判断这些元素是否是质数。
    0行：[0][0],[0][n-1]
    1行：[1][1],[1][n-2]
    2行：[2][2],[2][n-3]
    3行：[3][3],[3][n-4]
    ......
    
    如何判断一个数是否是质数？
    质数：只能被1和它本身整除的数。
    
"""

from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        m = len(nums)
        n = len(nums[0])
        max_prime = 0
        for i in range(m):
            for j in range(n):
                # 对角线上的元素
                if i == j or i + j == n - 1:
                    if self.isPrime(nums[i][j]):
                        max_prime = max(max_prime, nums[i][j])
        return max_prime
    
    # 判断一个数是否是质数
    def isPrime(self, num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
if __name__ == "__main__":
    s = Solution()
    print(s.diagonalPrime([[1,2,3],[5,6,7],[9,10,11]]))