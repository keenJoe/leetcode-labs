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
    
if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))