# 494. Target Sum


'''
    终止条件：
        1. 遍历完所有元素
        2. 当前元素的和为target
    选择列表：当选择当前元素时，可以选择加号或者减号
        1. 选择加号
        2. 选择减号
    路径：
        1. 当前元素的和
'''

from typing import List


class Solution:
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        result = 0
        
        def backtrack(index, current_sum):
            nonlocal result
            
            if index == len(nums):
                if current_sum == target:
                    result += 1
                return
            
            # for i in range(index, len(nums)):
            #     # 选择加号，自己还在想怎么选择
            #     backtrack(i + 1, current_sum + nums[i])
            #     # 选择减号
            #     backtrack(i + 1, current_sum - nums[i])            
            # 选择加号，自己还在想怎么选择
            # 这段代码使用了循环，会导致重复处理元素。在目标和问题中，我们需要为每个元素分配一个符号（+或-），而不是选择性地跳过某些元素。正确的代码应该是：
            backtrack(index + 1, current_sum + nums[index])
            # 选择减号
            backtrack(index + 1, current_sum - nums[index])            
        
        backtrack(0, 0)
        return result
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 使用字典缓存结果
        memo = {}
        
        def backtrack(index, current_sum):
            # 检查是否已计算过
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            # 选择加号
            plus = backtrack(index + 1, current_sum + nums[index])
            # 选择减号
            minus = backtrack(index + 1, current_sum - nums[index])
            
            # 缓存结果
            memo[(index, current_sum)] = plus + minus
            return memo[(index, current_sum)]
        
        return backtrack(0, 0)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.findTargetSumWays1([1,1,1,1,1], 3))
