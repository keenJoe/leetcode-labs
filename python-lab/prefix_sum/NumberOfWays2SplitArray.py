# 2270. Number of Ways to Split Array

from typing import List


class Solution:
    # nums = [10,4,-8,7]
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
    
        # 构建后缀和数组
        # suffix[i] 表示从 nums[i] 到 nums[n-1] 的和
        suffix = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        # 构建前缀和数组
        # prefix[i] 表示 nums[0] 到 nums[i] 的和
        prefix = [0] * (n + 1)  # 多一个位置，方便计算
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        count = 0
        for i in range(n):
            if i == 0:
                continue
            if prefix[i] >= suffix[i]:
                count += 1
        return count
    
    # 优化解法，思路一下打开，不需要构建后缀和数组，且易读
    def waysToSplitArray_1(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)  # 计算总和
        left_sum = 0
        count = 0
        
        # 遍历到倒数第二个元素即可，因为最后一个元素必须在右半部分
        for i in range(n - 1):
            left_sum += nums[i]
            right_sum = total - left_sum
            if left_sum >= right_sum:
                count += 1
                
        return count
