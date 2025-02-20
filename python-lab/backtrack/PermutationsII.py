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
            print("***************")
            print(path, visited)
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                print(i, nums[i], visited[i])
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
                print("pop: " + str(i), str(path), visited)
                print('--------------------------------')
        
        backtrack([], [False] * len(nums))
        return result
        
if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))
