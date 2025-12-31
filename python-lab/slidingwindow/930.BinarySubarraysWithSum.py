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
'''


from typing import List


# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         left = 0
#         sum = 0
#         count = 0

#         for right in range(len(nums)):
#             sum += nums[right]
#             if sum == goal:
#                 count += 1

#             while sum > goal:
#                 sum -= nums[left]
#                 left += 1
#                 if sum == goal:
#                     count += 1
#         return count

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            """统计和 <= k 的子数组个数"""
            if k < 0:
                return 0
            left = 0
            total = 0
            count = 0
            for right in range(len(nums)):
                total += nums[right]
                while total > k:
                    total -= nums[left]
                    left += 1
                # 关键：以 right 结尾、和 <= k 的子数组个数 = right - left + 1
                count += right - left + 1
            return count
        
        return atMost(goal) - atMost(goal - 1)


    def numSubarraysWithSum1(self, nums: List[int], goal: int) -> int:
        from collections import defaultdict
        
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # 空前缀
        
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            # 找之前有多少个前缀和 = prefix_sum - goal
            count += prefix_count[prefix_sum - goal]
            prefix_count[prefix_sum] += 1
        
        return count


    def numSubarraysWithSum2(self, nums: List[int], goal: int) -> int:
        left1 = 0  # 第一个使 sum <= goal 的位置
        left2 = 0  # 第一个使 sum < goal 的位置
        sum1 = 0
        sum2 = 0
        count = 0
        
        for right in range(len(nums)):
            sum1 += nums[right]
            sum2 += nums[right]
            
            # left1: 维护 sum1 <= goal
            while sum1 > goal and left1 <= right:
                sum1 -= nums[left1]
                left1 += 1
            
            # left2: 维护 sum2 < goal（严格小于）
            while sum2 >= goal and left2 <= right:
                sum2 -= nums[left2]
                left2 += 1
            
            # 以 right 结尾、和恰好等于 goal 的子数组个数
            count += left2 - left1
        
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubarraysWithSum([1,0,1,0,1], 2))
    print(solution.numSubarraysWithSum1([1,0,1,0,1], 2))
    print(solution.numSubarraysWithSum2([1,0,1,0,1], 2))