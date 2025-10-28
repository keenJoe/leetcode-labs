# 1423. Maximum Points You Can Obtain from Cards

'''
将 K 进行分割，如果从左侧拿 0 张，那么右侧则有 K 张；
以此类推
'''

from typing import List


class Solution:
    def maxScore1(self, cardPoints: List[int], k: int) -> int:
        current_sum = 0
        max_sum = 0
        length = len(cardPoints)
        for i in range(k + 1):
            left = i
            right = k - i
            current_sum = sum(cardPoints[0:left]) + sum(cardPoints[length - right:])
            max_sum = max(max_sum, current_sum)
        return max_sum

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        
        # 初始化：从右侧取 k 张牌的总和（left=0, right=k）
        current_sum = sum(cardPoints[length - k:])
        max_sum = current_sum
        
        # 滑动窗口：逐步用左侧的牌替换右侧的牌
        # i 表示从左侧取的牌数
        for i in range(1, k + 1):
            # 加上左侧第 i 张牌
            current_sum += cardPoints[i - 1]
            # 减去右侧最左边的一张牌
            current_sum -= cardPoints[length - k + i - 1]
            max_sum = max(max_sum, current_sum)
        
        return max_sum

if __name__ == "__main__":
    solution = Solution()
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    print(cardPoints[0:0])
    print(solution.maxScore(cardPoints, k))