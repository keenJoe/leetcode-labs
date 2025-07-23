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
            # 如果nums[i] == nums[j]，则j++
            if nums[i] == nums[j]:
                j += 1
            # 如果nums[i] != nums[j]，则i++，nums[i] = nums[j]，j++
            else:
                # 如果 i + 1 == j，相当于 i 和 j 此时指向同一个元素，赋值只是覆盖
                # 如果 i + 1 != j，相当于 i 和 j 此时指向不同的元素，赋值相当于覆盖了重复的元素
                i += 1
                if i != j:
                    # 将nums[j]赋值给nums[i]，相当于覆盖了重复的元素
                    nums[i] = nums[j]
                j += 1
        # 返回 i + 1 是因为 i 是索引，需要 +1 才是长度
        return i + 1
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2,3,3,4,5,5,6]
    print(solution.removeDuplicates(nums))
