# 1. Two Sum

'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

1、返回数组下标，而不是实际的值
2、不能使用两次相同的元素

可以使用哈希表，key 是 target - 数组元素，value 是数组下标。
如果当前元素在哈希表中，则返回当前元素和哈希表中元素的索引。
如果当前元素不在哈希表中，则将 target - 当前元素 和 当前元素的索引添加到哈希表中。

'''


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                return [hash_map[num], i]
            hash_map[target - num] = i
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(solution.twoSum([3, 2, 4], 6))  # [1, 2]
    print(solution.twoSum([3, 3], 6))  # [0, 1]