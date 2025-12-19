# 209. Minimum Size Subarray Sum

'''
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
'''

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = len(nums) + 1

        for right in range(len(nums)):
            current_sum += nums[right]

            # while current_sum >= target:
            #     min_length = min(min_length, right - left + 1)
            #     current_sum -= nums[left]
            #     left += 1
            while current_sum >= target:
                length = right - left + 1
                if length < min_length:
                    min_length = length
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0

if __name__ == "__main__":
    solution = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(solution.minSubArrayLen(target, nums))
    target = 4
    nums = [1,4,4]
    print(solution.minSubArrayLen(target, nums))
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print(solution.minSubArrayLen(target, nums))