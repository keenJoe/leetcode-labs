# 78. Subsets

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, path):
            result.append(path[:])
            
            for i in range(start, len(nums)):
                # 选择当前元素
                path.append(nums[i])
                # 递归
                backtrack(i + 1, path)
                # 回溯
                path.pop()
                
        backtrack(0, [])
        return result
    
if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))