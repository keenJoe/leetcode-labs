# 643. Maximum Average Subarray I

'''
1、初始化长度，最大平均值，当前窗口的和
2、开始从 k 位置遍历数组
3、判断加入当前元素后当前窗口长度是否大于 K，如果大于 K，则需要移动左指针，并更新当前窗口的和，然后计算平均值，并更新最大平均值
4、如果当前窗口长度小于 K，则直接计算平均值，并更新最大平均值
5、返回最大平均值
'''

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        max_average = float('-inf')
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        # 前 k 个元素的平均值
        max_average = current_sum / k

        for i in range(k, length):
            current_sum += nums[i] - nums[i - k]
            max_average = max(max_average, current_sum / k)

        return max_average

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(solution.findMaxAverage(nums, k))