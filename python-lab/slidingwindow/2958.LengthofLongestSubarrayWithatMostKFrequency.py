# 2958. Length of Longest Subarray With at Most K Frequency

'''
给你一个整数数组 nums 和一个整数 k 。

一个元素 x 在数组中的 频率 指的是它在数组中的出现次数。

如果一个数组中所有元素的频率都 小于等于 k ，那么我们称这个数组是 好 数组。

请你返回 nums 中 最长好 子数组的长度。

子数组 指的是一个数组中一段连续非空的元素序列。

 

示例 1：

输入：nums = [1,2,3,1,2,3,1,2], k = 2
输出：6
解释：最长好子数组是 [1,2,3,1,2,3] ，值 1 ，2 和 3 在子数组中的频率都没有超过 k = 2 。[2,3,1,2,3,1] 和 [3,1,2,3,1,2] 也是好子数组。
最长好子数组的长度为 6 。
示例 2：

输入：nums = [1,2,1,2,1,2,1,2], k = 1
输出：2
解释：最长好子数组是 [1,2] ，值 1 和 2 在子数组中的频率都没有超过 k = 1 。[2,1] 也是好子数组。
最长好子数组的长度为 2 。
示例 3：

输入：nums = [5,5,5,5,5,5,5], k = 4
输出：4
解释：最长好子数组是 [5,5,5,5] ，值 5 在子数组中的频率没有超过 k = 4 。
最长好子数组的长度为 4 。


需要使用哈希表记录元素的频率，如果遍历过程中元素的频率超过 k 值，那么就需要移动 left 值，直到当前的元素的频率满足 k 值

'''

from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_length = 0
        left = 0
        count = {}

        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubarrayLength([1,2,3,4,5], 2))