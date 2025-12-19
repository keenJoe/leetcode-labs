# 1658. Minimum Operations to Reduce X to Zero

'''
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。
请注意，需要 修改 数组以供接下来的操作使用。

如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

 

示例 1：
输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。

示例 2：
输入：nums = [5,6,7,8,9], x = 4
输出：-1

示例 3：
输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。


所以需要找到一个最长的子数组，使得子数组和为 x = sum(nums)
滑动窗口必须从最左或最右开始，因为只能删除最左或最右的元素
方案
先从左边开始删除。如果左边删除后，累计的元素和大于 x，那么回退，开始从右侧删除，如果右侧的累计元素同样大于 X，那么则返回-1
'''

from typing import List


# class Solution:
#     def minOperations(self, nums: List[int], x: int) -> int:
#         left = 0
#         right = len(nums) - 1
        
#         left_operations = 0
#         right_operations = 0

#         left_sum = 0
#         right_sum = 0

#         while left <= right:
#             if left_sum == right_sum == x:
#                 return min(left_operations, right_operations)
#             elif left_sum == x:
#                 return left_operations
#             elif right_sum == x:
#                 return right_operations

#             if left_sum + nums[left] <= x:
#                 left_sum += nums[left]
#                 left += 1
#                 left_operations += 1
#             elif left_sum + nums[right] <= x:
#                 left_sum += nums[right]
#                 right -= 1
#                 left_operations += 1
            
#             if right_sum + nums[right] <= x:
#                 right_sum += nums[right]
#                 right -= 1
#                 right_operations += 1
#             elif right_sum + nums[left] <= x:
#                 right_sum += nums[left]
#                 left += 1
#                 right_operations += 1

#             # if current_sum + nums[left] <= x:
#             #     current_sum += nums[left]
#             #     left += 1
#             #     operations += 1
#             # elif current_sum + nums[right] <= x:
#             #     current_sum += nums[right]
#             #     right -= 1
#             #     operations += 1
#             # else:
#             #     return -1
        
#         return -1

'''
正确解法：逆向思维 + 滑动窗口
核心思路：移除两端的元素使其和为 x，等价于保留中间的连续子数组使其和为 sum(nums) - x。因此，找最长的中间子数组使其和为 target = sum(nums) - x，答案就是 len(nums) - maxLen。
'''

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        
        # 特殊情况
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        # 滑动窗口找和为 target 的最长子数组
        left = 0
        current_sum = 0
        max_len = -1
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # 当窗口和超过 target 时，收缩左边界
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            
            # 找到和为 target 的子数组
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len if max_len != -1 else -1

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,4,2,3]
    x = 5
    print(solution.minOperations(nums, x))