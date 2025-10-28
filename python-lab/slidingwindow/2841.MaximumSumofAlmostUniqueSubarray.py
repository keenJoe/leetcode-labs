# 2841. Maximum Sum of Almost Unique Subarray

'''
给你一个整数数组 nums 和两个正整数 m 和 k 。

请你返回 nums 中长度为 k 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 0 。

如果 nums 的一个子数组有至少 m 个互不相同的元素，我们称它是 几乎唯一 子数组。

子数组指的是一个数组中一段连续 非空 的元素序列。

 

示例 1：

输入：nums = [2,6,7,3,1,7], m = 3, k = 4
输出：18
解释：总共有 3 个长度为 k = 4 的几乎唯一子数组。分别为 [2, 6, 7, 3] ，[6, 7, 3, 1] 和 [7, 3, 1, 7] 。这些子数组中，和最大的是 [2, 6, 7, 3] ，和为 18 。
示例 2：

输入：nums = [5,9,9,2,4,5,4], m = 1, k = 3
输出：23
解释：总共有 5 个长度为 k = 3 的几乎唯一子数组。分别为 [5, 9, 9] ，[9, 9, 2] ，[9, 2, 4] ，[2, 4, 5] 和 [4, 5, 4] 。这些子数组中，和最大的是 [5, 9, 9] ，和为 23 。
示例 3：

输入：nums = [1,2,1,2,1,2,1], m = 3, k = 3
输出：0
解释：输入数组中不存在长度为 k = 3 的子数组含有至少  m = 3 个互不相同元素的子数组。所以不存在几乎唯一子数组，最大和为 0 。
'''

from typing import List


class Solution:
    # 错误❌解法
    def maxSum1(self, nums: List[int], m: int, k: int) -> int:
        current_sum = 0
        max_sum = 0
        # 使用字典，而不是set。因为 set 会导致元素仍旧存在但是被移出
        unique_set = set()
        left, right = 0, 0

        for i in range(len(nums)):
            current_sum += nums[i]
            unique_set.add(nums[i])
            right = i + 1

            # 边界混乱，要区分 == K 和 > K 的情况
            if right - left == k:
                if len(unique_set) >= m:
                    max_sum = max(max_sum, current_sum)
                    # 如果一直都是相同的元素，此时移除，就会导致集合为空
                    unique_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        return max_sum

    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        current_sum = 0
        max_sum = 0
        count = {}  # 使用字典记录每个元素出现的次数
        left = 0
        
        for right in range(len(nums)):  # 遍历整个数组
            # 添加右边界元素
            current_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1
            
            # 当窗口大小超过 k 时，移除左边界
            if right - left + 1 > k:
                current_sum -= nums[left]
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]  # 计数为0时才删除
                left += 1
            
            # 当窗口大小等于 k 时，检查是否满足条件
            if right - left + 1 == k:
                if len(count) >= m:  # 检查不同元素的个数
                    max_sum = max(max_sum, current_sum)
        
        return max_sum

if __name__ == "__main__":
    solution = Solution()
    nums = [2,6,7,3,1,7]
    m = 3
    k = 4
    print(solution.maxSum(nums, m, k))

    nums = [5,9,9,2,4,5,4]
    m = 1
    k = 3
    print(solution.maxSum(nums, m, k))

    nums = [1,2,1,2,1,2,1]
    m = 3
    k = 3
    print(solution.maxSum(nums, m, k))

    nums = [4,4,4,4]
    m = 2
    k = 3
    print(solution.maxSum(nums, m, k))


    nums = [1,1,1,3]
    m = 2
    k = 2
    print(solution.maxSum(nums, m, k))