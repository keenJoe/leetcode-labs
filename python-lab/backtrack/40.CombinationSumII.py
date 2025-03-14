# 40. Combination Sum II

'''
    candidates 中的每个数字在每个组合中只能使用一次 。
    可以使用一个数组记录每个数字是否使用过，避免重复使用。
    
    给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

    candidates 中的每个数字在每个组合中只能使用 一次 。（不能像39.CombinationSum.py那样，无限选择同一个元素）

    注意：解集不能包含重复的组合。 
'''

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(path, start, remain):
            if remain == 0:
                result.append(path[:])
                return
            
            # 还有一个关键点是range从start开始，避免重复使用前面的数字
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                
                # 去重：跳过同一层的重复数字
                # i > start 表示现在是同层，而且同层的第一个元素已经遍历完；
                # 如果不加 i > start， 会导致后面重复的元素被跳过
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                # 因为每个元素只能使用一次，所以i+1
                backtrack(path, i + 1, remain - candidates[i])
                path.pop()

        backtrack([], 0, target)
        return result

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    solution = Solution()
    print(solution.combinationSum2(candidates, target))
    
    candidates = [2,5,2,1,2]
    target = 5
    solution = Solution()
    print(solution.combinationSum2(candidates, target))
    
    candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 30
    solution = Solution()
    print(solution.combinationSum2(candidates, target))