# 35. Search Insert Position

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

要求时间复杂度为 O(log n)，因此不能使用线性搜索，要是用二分查找。

如果 target 不存在，则返回它将会被按顺序插入的位置。
"""


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 5))
    print(solution.searchInsert([1, 3, 5, 6], 2))
    print(solution.searchInsert([1, 3, 5, 6], 7))
    print(solution.searchInsert([1, 3, 5, 6], 0))
    print(solution.searchInsert([1], 0))
    print(solution.searchInsert([1], 1))
    print(solution.searchInsert([1], 2))