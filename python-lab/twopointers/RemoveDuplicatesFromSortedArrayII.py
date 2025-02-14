# 80. Remove Duplicates from Sorted Array II

"""
1、要求原地删除，不能使用额外空间，那是不是意味着我需要移动元素呢？

"""


from typing import List


class Solution:
    def removeDuplicates_1(self, nums: List[int]) -> int:
        fast = 1
        slow = 0
        count = 1

        while fast < len(nums):
            if nums[fast] == nums[slow]:
                if fast - slow <= 1:
                    count += 1
                    fast += 1
                else:
                    fast += 1
            else:
                slow = fast
                fast += 1
                count += 1

        return count
    

    def removeDuplicates(self, nums: List[int]) -> int:
        # 如果数组长度小于等于2，不需要处理
        if len(nums) <= 2:
            return len(nums)
        
        # 慢指针指向将要被填入的位置
        slow = 2
        # 快指针用于遍历数组
        for fast in range(2, len(nums)):
            # 如果当前元素与倒数第二个保留的元素不相同，说明可以保留当前元素
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 1, 1, 1, 2, 2, 3]
    print(solution.removeDuplicates(nums))


    [0, 1, 1, 1, 1, 2, 2, 3]
    [0, 1, 1, 2, 1, 2, 2, 3]
    [0, 1, 1, 2, 2, 2, 2, 3]
    [0, 1, 1, 2, 2, 3, 2, 3]
