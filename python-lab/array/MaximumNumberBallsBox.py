# 1742. Maximum Number of Balls in a Box

'''
    1、遍历数组，计算每个数字的各个位的和；
    2、使用一个字典来存储每个位的和出现的次数；
    3、返回字典中出现次数最多的那个位的和。
'''

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ball_count = {}
        for i in range(lowLimit, highLimit + 1):
            sum = 0
            while i > 0:
                sum += i % 10
                i //= 10
            ball_count[sum] = ball_count.get(sum, 0) + 1
        
        return max(ball_count.values())


if __name__ == "__main__":
    solution = Solution()
    print(solution.countBalls(1, 10))
