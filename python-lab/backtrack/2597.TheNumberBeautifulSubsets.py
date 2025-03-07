# 2597. The Number of Beautiful Subsets

'''
    1、暴力回溯
        1、选择当前元素加入到subset中
        2、计算当前subset的美丽值
        3、如果当前的美丽值不等于k，则ans+1
        4、如果当前的美丽值等于k，则直接返回
        5、回溯
    2、动态规划
'''

from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def is_beautiful(subset):
            # 检查子集中是否存在差值为k的两个数
            for i in range(len(subset)):
                for j in range(i + 1, len(subset)):
                    if abs(subset[i] - subset[j]) == k:
                        return False
            return True
        
        ans = 0  # 包含空集
        subset = []
        
        def backtrack(index):
            nonlocal ans
            
            # 当前子集是否美丽
            if is_beautiful(subset):
                ans += 1
            
            # 继续添加元素
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return ans - 1  # 减去空集

if __name__ == "__main__":
    solution = Solution()
    print(solution.beautifulSubsets([4,2,5,9,10,3], 1))