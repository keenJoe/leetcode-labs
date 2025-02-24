# 40. Combination Sum II

'''
    candidates 中的每个数字在每个组合中只能使用一次 。
    可以使用一个数组记录每个数字是否使用过，避免重复使用。
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
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
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