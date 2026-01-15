# 53. Maximum Subarray

'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
'''

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix_sum = 0
        max_subarray_sum = float('-inf')
        
        for num in nums:   
            prefix_sum += num
            max_subarray_sum = max(max_subarray_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            
        return max_subarray_sum
    
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    print(solution.maxSubArray([1]))  # Output: 1
    print(solution.maxSubArray([5,4,-1,7,8]))  # Output: 23