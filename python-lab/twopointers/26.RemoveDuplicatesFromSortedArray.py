# 26. Remove Duplicates from Sorted Array

"""
    使用双指针
    要原地删除重复的元素，返回新数组的长度。
    1 1 2
    两个指针分别从0和1开始，
    如果nums[i] == nums[j]，则j++
    如果nums[i] != nums[j]，则i++，nums[i] = nums[j]，j++
    最后返回i+1
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2]
    print(solution.removeDuplicates(nums))
