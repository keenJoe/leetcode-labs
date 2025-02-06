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
'''

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        
        def backtrack(path):
            if len(path) == length:
                result.append(path[:])
                return
            
            for i in range(length):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(path)
                path.pop()
        
        backtrack([])
        return result
    
    
    # 使用visited数组来判断元素是否已经用过
    # 但是也没有优化太多
    def permute_2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, visited):
            if len(path) == len(nums):
                yield path[:]
                return
            
            for i in range(len(nums)):
                if visited[i]:  # 使用O(1)时间复杂度检查是否访问过
                    continue
                visited[i] = True
                path.append(nums[i])
                yield from backtrack(path, visited)
                path.pop()
                visited[i] = False
        
        return list(backtrack([], [False] * len(nums)))
    
    # 交换法
    def permute_3(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            print('***********')
            print('nums', nums)
            print('first', first)
            if first == n:  
                res.append(nums[:])
                return
            
            for i in range(first, n):
                print('i', i)
                # 交换，将当前数字放到first位置
                nums[first], nums[i] = nums[i], nums[first]
                # 递归填下一个位置
                backtrack(first + 1)
                # 回溯，恢复原状
                nums[first], nums[i] = nums[i], nums[first]
                print('===========')
                print('back nums', nums)
                print('back first', first)
                print('back i', i)
                print('===========')
        
        n = len(nums)
        res = []
        backtrack()
        return res
    
if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute_3(nums))