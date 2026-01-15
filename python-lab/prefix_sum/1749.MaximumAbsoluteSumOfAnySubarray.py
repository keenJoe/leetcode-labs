# 1749. Maximum Absolute Sum of Any Subarray

'''
给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl + numsl+1 + ... + numsr-1 + numsr) 。

请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。

abs(x) 定义如下：

如果 x 是负整数，那么 abs(x) = -x 。
如果 x 是非负整数，那么 abs(x) = x 。
 

示例 1：

输入：nums = [1,-3,2,3,-4]
输出：5
解释：子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5 。
示例 2：

输入：nums = [2,-5,1,-4,3,-2]
输出：8
解释：子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8 。
'''

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        # 前缀和和原始数组的关系不大，一定要遵循前缀和的计算逻辑。
        # 如果不多申请一个位置，那么这个前缀和计算出来是错误的。
        prefix_num : List[int] = [0] * (len(nums) + 1)  # 多申请一个位置存储空前缀
        prefix_num[0] = 0  # 空前缀和为0
        for i in range(1, len(nums) + 1):
            prefix_num[i] = prefix_num[i - 1] + nums[i - 1]
            
        max_sum = float('-inf')
        min_sum = float('inf')
        for i in range(len(prefix_num)):
            max_sum = max(max_sum, prefix_num[i])
            min_sum = min(min_sum, prefix_num[i])
        
        return max_sum - min_sum
    
    
    def maxAbsoluteSum1(self, nums: List[int]) -> int:
        # 使用前缀和方法
        # 任意子数组和 = prefix[r] - prefix[l]
        # 要使绝对值最大，需要找 max(prefix) - min(prefix)
        # 注意：需要包含 prefix[0] = 0（空前缀）
        
        prefix_sum = 0
        max_sum = 0  # 初始化为0，代表空前缀
        min_sum = 0  # 初始化为0，代表空前缀
        
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum)
            min_sum = min(min_sum, prefix_sum)
        
        return max_sum - min_sum
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxAbsoluteSum([1, -3, 2, 3, -4]))  # Output: 5
    print(solution.maxAbsoluteSum([-2, -5, 6, -2, -3, 1, 5, -6]))  # Output: 7