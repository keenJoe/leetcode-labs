# 3634. Minimum Removals to Balance Array

'''
给你一个整数数组 nums 和一个整数 k。

如果一个数组的 最大 元素的值 至多 是其 最小 元素的 k 倍，则该数组被称为是 平衡 的。

你可以从 nums 中移除 任意 数量的元素，但不能使其变为 空 数组。

返回为了使剩余数组平衡，需要移除的元素的 最小 数量。

注意：大小为 1 的数组被认为是平衡的，因为其最大值和最小值相等，且条件总是成立。

1、先排序
2、维护一个滑动窗口，left = 0 right = 1
3、如果 nums[right] < nums[left] * k，则移动 right
'''

from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        max_len = 1
        
        for right in range(n):
            # 当窗口不满足条件时，收缩左边界
            while nums[right] > nums[left] * k:
                left += 1
            max_len = max(max_len, right - left + 1)
        
        return n - max_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.minRemoval([1,2,3,4,5], 2))