# 47. Permutations II

# 输入：nums = [1,1,2]
# 输出：[[1,1,2],[1,2,1],[2,1,1]]

# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# 有重复元素，需要去重

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
        
if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))
