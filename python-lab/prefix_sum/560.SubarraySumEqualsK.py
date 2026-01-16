# 560. Subarray Sum Equals K

'''
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2


1、构建一个前缀和数组，每个位置的元素都是从原数组的 0 位置开始累加得到值
2、遍历前缀和数组
    1、如果当前位置的值等于 k，则计数加 1
    2、然后开始从 i + 1 的位置继续遍历，使用当前位置的值减去i 位置的值，是否等于 k，如果等于 k，则计数加 1
3、返回计数
'''

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))