# 283. Move Zeroes


"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

前后两个指针，如果前指针遇到0，则后指针开始移动，直到遇到非0，然后交换两个指针的值，然后前指针继续移动，直到数组结束。
"""


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = 0
        tail = len(nums) - 1

        while prev < tail:
            if nums[prev] == 0:
                while nums[tail] == 0:
                    tail -= 1
                nums[prev], nums[tail] = nums[tail], nums[prev]
            prev += 1


    """
        两个指针都从0开始。
        如果前指针遇到0，则后指针开始移动，直到遇到非0，然后交换两个指针的值。
        然后将前指针移动到后指针的位置，继续遍历。
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        second = 0

        while second < len(nums):
            if nums[first] == 0:
                while second < len(nums) and nums[second] == 0:
                    second += 1
                if second < len(nums):
                    nums[first], nums[second] = nums[second], nums[first]
            first += 1
            second += 1


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)
        