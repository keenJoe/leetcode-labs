# 47. Permutations II

'''
    最重要的一点是如果两个数字相同，并且前一个数字没有被使用，那么第二个数字不能被使用，需要跳过；
'''

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        def backtrack(path, visited):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                # 如果当前数字和前一个数字相同，并且前一个数字没有被使用，则跳过
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                path.append(nums[i])
                backtrack(path, visited)
                path.pop()
                visited[i] = False
        
        backtrack([], [False] * len(nums))
        return result
    
    def permuteUnique_swap(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
                return
                
            # 用于记录当前层使用过的数字
            # 关键点：
                # 1. 如果当前数字已经在当前层使用过，跳过
                # 2. 如果当前数字和前一个数字相同，并且前一个数字没有被使用，则跳过
            # 因为每次都是初始化一个新的used，所以不会出现重复使用的情况
            used = set()
            
            for i in range(first, n):
                # 如果当前数字已经在当前层使用过，跳过
                if nums[i] in used:
                    continue
                    
                used.add(nums[i])
                # 交换
                nums[first], nums[i] = nums[i], nums[first]
                # 递归
                backtrack(first + 1)
                # 回溯，恢复原状
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        nums.sort()  # 排序以便于处理重复元素
        backtrack()
        return res
        
if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))
