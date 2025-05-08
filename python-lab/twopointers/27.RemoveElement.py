# 27. Remove Element

"""
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

    假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

    更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
    返回 k。
    
    有两点需要注意
    1、要移除元素，元素的顺序可能发生改变
    2、返回的是不等于val的元素的数量，而不是新数组的长度
    
    使用双指针思想
    如果nums[i] != val，则i++，j++
    如果nums[i] == val，那么需要找到一个不等于val的元素，然后交换nums[i]和nums[j]，i++，j++
    如何找到一个不等于val的元素？
    使用一个指针j，从i+1开始，找到一个不等于val的元素，然后交换nums[i]和nums[j]，i++，j++
    最后返回i
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == val:
                while j < len(nums) and nums[j] == val:
                    j += 1
                    
                # 关键在于找到后一定要交换，否则会死循环
                if j < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            else:
                i += 1
                j += 1
        return i
    
    
    # 使用快慢指针，会覆盖元素，但是不会改变元素的顺序
    def removeElement1(self, nums: List[int], val: int) -> int:
        # 使用快慢指针
        slow = 0
        for fast in range(len(nums)):
            # 如果当前元素不等于val，则保留
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
                    


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(solution.removeElement(nums, val))
    
    nums = [2, 2, 2]
    val = 3
    print(solution.removeElement(nums, val))
    
    nums = [2, 2]
    val = 3
    print(solution.removeElement(nums, val))
    
    nums = [2]
    val = 3
    print(solution.removeElement(nums, val))
