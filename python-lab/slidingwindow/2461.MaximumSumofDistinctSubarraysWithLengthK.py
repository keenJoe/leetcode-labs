# 2461. Maximum Sum of Distinct Subarrays With Length K


'''
给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：

子数组的长度是 k，且
子数组中的所有元素 各不相同 。
返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。

子数组 是数组中一段连续非空的元素序列。

毫无疑问要是用滑动窗口。
这里关键的点是如何确定窗口内所有元素都不重复。
也就是说必须每一个元素的数量都是 1

'''

from typing import Counter, List


class Solution:
    def maximumSubarraySum2(self, nums: List[int], k: int) -> int:
        current_sum = 0
        max_sum = 0
        left = 0
        count = {}

        for right in range(len(nums)):
            current_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1
            if count[nums[right]] > 1 or right - left + 1 > k:
                current_sum -= nums[left]
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            if right - left + 1 == k:
                if len(count) == k:
                    max_sum = max(max_sum, current_sum)
            
        return max_sum

    def maximumSubarraySum2(self, nums: List[int], k: int) -> int:
        current_sum = 0
        max_sum = 0
        count = {}

        for right in range(len(nums)):
            # 加入右边界
            current_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1
            
            # 窗口超过 k 时移除左边界
            if right >= k:
                left_val = nums[right - k]
                current_sum -= left_val
                count[left_val] -= 1
                if count[left_val] == 0:
                    del count[left_val]
            
            # 窗口大小为 k 且无重复
            if right >= k - 1 and len(count) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum

    from collections import Counter

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = sum(nums[:k])
        count = Counter(nums[:k])
        
        if len(count) == k:
            max_sum = current_sum
        
        for i in range(k, len(nums)):
            # 滑动窗口
            current_sum += nums[i] - nums[i - k]
            count[nums[i]] += 1
            count[nums[i - k]] -= 1
            if count[nums[i - k]] == 0:
                del count[nums[i - k]]
            
            if len(count) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum


if __name__ == "__main__":
    solution = Solution()
    nums = [1,5,4,2,9,9,9]
    k = 3
    print(solution.maximumSubarraySum(nums, k))