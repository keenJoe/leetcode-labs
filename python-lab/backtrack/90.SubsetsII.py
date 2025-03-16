# 90. Subsets II
# nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# 思路：
    # 1. 先排序
    # 2. 使用回溯法，记录当前路径和当前路径的元素个数
    # 3. 如果当前路径的元素个数等于nums的长度，则将当前路径加入结果集
    # 4. 如果当前路径的元素个数小于nums的长度，则继续回溯

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # 先排序，这样相同的数字会相邻
        
        def backtrack(start, path):
            result.append(path[:])  # 把当前路径加入结果集
            
            used = set()
            for i in range(start, len(nums)):
                # 跳过重复元素，但要保留第一个
                if nums[i] in used:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1, path)  # 递归
                path.pop()  # 回溯，移除最后添加的元素
        
        backtrack(0, [])
        return result
    
    
    def subsetsWithDup_1(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        def backtrack(start, path):
            # 终止条件
            result.append(path[:])
            
            for i in range(start, len(nums)):
                # i > start 表示当前元素不是第一个元素，nums[i] == nums[i-1] 表示当前元素和前一个元素相同，则跳过
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1,path)
                path.pop()
        
        backtrack(0, [])
        return result
    
if __name__ == "__main__":
    nums = [1,2,2]
    print(Solution().subsetsWithDup(nums))
    print(Solution().subsetsWithDup_1(nums))