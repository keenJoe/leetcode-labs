# 2441. Largest Positive Integer That Exists With Its Negative

'''
给你一个不包含任何零的整数数组 nums ，找出自身与对应的负数都在数组中存在的最大正整数 k 。

返回正整数 k ，如果不存在这样的整数，返回 -1 。

示例 1：
输入：nums = [-1,2,-3,3]
输出：3
解释：3 是数组中唯一一个满足题目要求的 k 。

示例 2：
输入：nums = [-1,10,6,7,-7,1]
输出：7
解释：数组中存在 1 和 7 对应的负数，7 的值更大。

示例 3：
输入：nums = [-10,8,6,7,-2,-3]
输出：-1
解释：不存在满足题目要求的 k ，返回 -1 。
'''

from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_k = -1
        num_set = set() 
        for i in range(len(nums)):
            if nums[i] in num_set:
                max_k = max(max_k, abs(nums[i]))
            num_set.add(-nums[i])

        return max_k

    def findMaxK_1(self, nums: List[int]) -> int:
        max_k = -1
        
        sorted_nums = sorted(nums)
        left = 0
        right = len(sorted_nums) - 1
        while left < right:
            # if sorted_nums[left] + sorted_nums[right] == 0:
            #     max_k = max(max_k, sorted_nums[right])
            #     left += 1
            #     right -= 1
            # elif sorted_nums[left] + sorted_nums[right] < 0:
            #     left += 1
            # else:
            #     right -= 1
            total = sorted_nums[left] + sorted_nums[right]
            if total == 0:
                return sorted_nums[right]  # 直接返回，不用继续
            elif total < 0:
                left += 1
            else:
                right -= 1
        return max_k

    # 确实是更牛逼的方案
    def findMaxK_2(self, nums: List[int]) -> int:
        seen = set(nums)  # 一次性构建 Set
        max_k = -1
        
        for num in nums:
            if num > 0 and -num in seen:
                max_k = max(max_k, num)
        
        return max_k

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxK_1([-1,2,-3,3]))
    print(solution.findMaxK_1([-1,10,6,7,-7,1]))
    print(solution.findMaxK_1([-10,8,6,7,-2,-3]))