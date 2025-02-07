# 2239. Find Closest Number to Zero

from typing import List

class Solution:
    # 使用lambda表达式，先按绝对值排序，再按负数排序
    # 但是这种做法是不是太慢了，不是最优的解。
    def findClosestNumber(self, nums: List[int]) -> int:
        return min(nums, key=lambda x: (abs(x), -x))

    # 暴力解法，遍历数组，找到最接近0的数
    def findClosestNumber_2(self, nums: List[int]) -> int:
        min_num = nums[0]
        for num in nums:
            if abs(num) < abs(min_num):
                min_num = num
            elif abs(num) == abs(min_num) and num > min_num:
                min_num = num

        return min_num
    
    
    
