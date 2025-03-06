# 491. Non-decreasing Subsequences

from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        # nums.sort()
        
        # 回溯函数
        def backtrack(index, path, used):
            # 终止条件
            if len(path) >= 2:
                res.append(path[:])
                
            # 选择列表
            for i in range(index, len(nums)):
                # 两种不同的标记方式
                # 使用布尔数组标记已使用元素：[False] * len(nums)
                # 使用集合标记当前层已使用的值：used = set()
                # 为什么布尔数组标记不足够
                # 布尔数组标记的是位置，而不是值。这在处理重复元素时会出现问题。
                
                # 因为允许重复元素，所以不能使用布尔数组标记。因为布尔数组是全局的，不能保证当前层使用过的元素在下一层不会被使用。
                if used[i] or nums[i] in path:
                    continue
                
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(i + 1, path, used)
                    path.pop()
                    used[i] = False
                
        backtrack(0, [], [False] * len(nums))
        return res


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        # nums.sort()
        
        # 回溯函数
        def backtrack(start, path):
            # 终止条件
            if len(path) >= 2:
                res.append(path[:])
                
            used = set()  # 记录当前层使用过的值
            for i in range(start, len(nums)):
                # 如果当前值在当前层已使用过，跳过
                if nums[i] in used:
                    continue
                
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])  # 标记当前值已在当前层使用
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
                    # 注意：不需要从used中移除，因为used只对当前层有效
        
        backtrack(0, [])
        return res
    
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubsequences([4,6,7,7]))
    print(solution.findSubsequences([4,4,3,2,1]))
    print(solution.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]))