# 3095. Shortest Subarray With OR at Least K I

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1 if nums else -1
        
        # 暴力解法
        min_length = float('inf')
        for i in range(len(nums)):
            for j in range(len(nums)):
                if self.or_value(nums[i:j+1]) >= k:
                   length = j - i + 1
                   min_length = min(min_length, length)
        return min_length if min_length != float('inf') else -1
    
    def or_value(self, nums: List[int]) -> int:
        value = 0
        for num in nums:
            value |= num
        return value

    # 滑动窗口
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # 特殊情况处理：当k=0时，任何长度为1的子数组都满足条件
        if k == 0:
            return 1 if nums else -1
            
        n = len(nums)
        min_length = float('inf')
        left = 0
        current_or = 0
        
        for right in range(n):
            current_or |= nums[right]
            
            while left <= right and current_or >= k:
                min_length = min(min_length, right - left + 1)
                
                new_or = 0
                for i in range(left + 1, right + 1):
                    new_or |= nums[i]
                
                if new_or >= k:
                    current_or = new_or
                    left += 1
                else:
                    break
        
        return min_length if min_length != float('inf') else -1