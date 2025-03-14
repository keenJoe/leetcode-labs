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
    
    
    给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

    candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

    对于给定的输入，保证和为 target 的不同组合数少于 150 个。
    
    
    终止条件：
        如果当前路径和等于target，则将路径加入结果中，并返回
        如果当前路径和大于target，则跳过该元素，继续选择下一个元素，触发回溯
    遍历每一个元素
    选择当前元素，加入路径中
    递归，开始选择下个元素
    回溯，移除最后一个元素
    重复3-5，直到所有元素都用过一次
    返回结果
'''

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(start, path, remain):
            if remain == 0:
                result.append(path[:])
                return
            
            # 剪枝，如果当前路径和大于target，则跳过该元素，继续选择下一个元素，触发回溯
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                # 提前剪枝，如果当前元素大于remain，则跳过该元素，继续选择下一个元素
                if candidates[i] > remain:
                    break
                
                path.append(candidates[i])
                # 不需要i+1，因为可以重复选择同一个元素，可以无限选择
                backtrack(i, path, remain - candidates[i])
                path.pop()
            
        backtrack(0, [], target)
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