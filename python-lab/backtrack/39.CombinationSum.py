# 39. Combination Sum

'''
    1、回溯法
    2、先排序
    3、遍历数组，选择一个元素加入路径中
        如果路径的所有元素的和等于target，则将路径加入结果中，并返回；
        如果路径的所有元素的和大于target，则跳过该元素，继续选择下一个元素；
        如果路径的所有元素的和小于target，则继续选择下一个元素；
    4、递归，开始选择下个元素
    5、回溯，移除最后一个元素
    6、重复3-5，直到所有元素都用过一次
    7、返回结果
'''

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(path, start):
            if sum(path) == target:
                result.append(path[:])
                return
            
            if sum(path) > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(path, i)
                path.pop()
                
        backtrack([], 0)
        return result
    
    
    # 2、回溯法，提前剪枝，避免重复计算
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # 保持排序，便于剪枝
        
        def backtrack(path, start, remain):
            # 剪枝：如果当前数字已经大于剩余目标值，后面的数字更大，直接break，不需要之前的两个if判断
            if remain == 0:  # 使用remain代替sum(path)
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # 剪枝：如果当前数字已经大于剩余目标值，后面的数字更大，直接break
                if candidates[i] > remain:
                    break
                    
                path.append(candidates[i])
                # remain - candidates[i] 传递剩余值，避免重复计算sum
                backtrack(path, i, remain - candidates[i])
                path.pop()
                
        backtrack([], 0, target)
        return result

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    solution = Solution()
    print(solution.combinationSum(candidates, target))
    
    candidates = [2,3,5]
    target = 8
    solution = Solution()
    print(solution.combinationSum(candidates, target))
    
    candidates = [2]
    target = 1
    solution = Solution()
    print(solution.combinationSum(candidates, target))
    
    candidates = [2]
    target = 2
    solution = Solution()
    print(solution.combinationSum(candidates, target))