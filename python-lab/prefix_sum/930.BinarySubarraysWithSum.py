# 930. Binary Subarrays With Sum

'''
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。

子数组 是数组的一段连续部分。

 

示例 1：

输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
示例 2：

输入：nums = [0,0,0,0,0], goal = 0
输出：15


暴力法：
    使用两个 for 循环解决，但是时间复杂度为 O(n^2)，会超时。

goal - prefix_sum in map: 如果存在，则计数加 1
prefix_sum not in map: 则将 prefix_sum 加入 map


'''

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        prefix_map = {0: 1}
        count = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in prefix_map:
                count += prefix_map[prefix_sum - goal]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count

if '__name__' == '__main__':
    solution = Solution()
    print(solution.numSubarraysWithSum([1,0,1,0,1], 2))