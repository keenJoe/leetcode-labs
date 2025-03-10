# 2012. Sum of Beauty in the Array

'''
    给你一个下标从 0 开始的整数数组 nums 。对于每个下标 i（1 <= i <= nums.length - 2），nums[i] 的 美丽值 等于：
        2，对于所有 0 <= j < i 且 i < k <= nums.length - 1 ，满足 nums[j] < nums[i] < nums[k]
        1，如果满足 nums[i - 1] < nums[i] < nums[i + 1] ，且不满足前面的条件
        0，如果上述条件全部不满足
        
        返回符合 1 <= i <= nums.length - 2 的所有 nums[i] 的 美丽值的总和 。
'''


from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:  # 处理边界情况
            return 0
        
        # 预处理右侧最小值
        right_min = [float('inf')] * n
        curr_min = nums[-1]
        for i in range(n-2, -1, -1):
            right_min[i] = curr_min
            curr_min = min(curr_min, nums[i])
        
        # 在一次遍历中计算美丽值
        result = 0
        left_max = nums[0]
        
        # 遍历计算每个元素的美丽值
        for i in range(1, n-1):
            # 检查是否满足美丽值为2的条件
            if left_max < nums[i] < right_min[i]:
                result += 2
            # 检查是否满足美丽值为1的条件
            elif nums[i-1] < nums[i] < nums[i+1]:
                result += 1
            # 更新左侧最大值
            left_max = max(left_max, nums[i])
        
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfBeauties([1,2,3]))
    print(solution.sumOfBeauties([2,4,6,4]))
    print(solution.sumOfBeauties([3,2,1]))