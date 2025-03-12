# 46. Permutations
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 所有元素都要用一次，且每个元素只能用一次
'''
    0、如果路径长度等于数组长度，则将路径加入结果中。
    1、遍历数组，选择一个元素加入路径中。
    2、递归，开始选择下个元素。如果元素已经用过，则跳过。如何判断元素已经用过？
        通过判断是否在队列中。
    3、回溯，移除最后一个元素。
    4、重复1-3，直到所有元素都用过一次。
    5、返回结果。
    
    给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
    
    全排列：
        每个元素都要使用一次
        每次都要从头开始遍历
'''

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(path, visited):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            # 开始遍历
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])
                backtrack(path, visited)
                path.pop()
                visited[i] = False
        
        backtrack([], [False] * len(nums))  
        return result
    
    # 交换法
    def permute_3(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:  
                res.append(nums[:])
                return
            
            for i in range(first, n):
                # 交换，将当前数字放到first位置
                nums[first], nums[i] = nums[i], nums[first]
                # 递归填下一个位置
                backtrack(first + 1)
                # 回溯，恢复原状
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res

    
    
if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute_3(nums))