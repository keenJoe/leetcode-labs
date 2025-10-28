# 1423. Maximum Points You Can Obtain from Cards

'''
将 K 进行分割，如果从左侧拿 0 张，那么右侧则有 K 张；
以此类推
'''

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        current_sum = 0
        max_sum = 0
        length = len(cardPoints)
        for i in range(k + 1):
            left = i
            right = k - i
            current_sum = sum(cardPoints[0:left]) + sum(cardPoints[length - right:])
            max_sum = max(max_sum, current_sum)
        return max_sum

if __name__ == "__main__":
    solution = Solution()
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    print(cardPoints[0:0])
    print(solution.maxScore(cardPoints, k))