# 1493. Longest Subarray of 1's After Deleting One Element

'''
给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

1、需要找到两个1之间的最大距离，且只能包含一个 0
    与其说是“找两个 1 之间的距离”，不如说是 “维护一个最长的连续子数组，该子数组中最多只允许包含一个 0”。
    这个思路就很明确了
2、通过 0 进行分组，然后找到两个长度最大的子数组，然后返回两个子数组的长度之和
'''

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        left = 0
        right = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length - 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubarray([1,1,0,1]))