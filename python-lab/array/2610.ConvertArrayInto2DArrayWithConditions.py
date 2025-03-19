# 2610. Convert an Array Into a 2D Array With Conditions


"""
    1、使用一个字典来记录每个数字出现的次数。
    2、记录最大出现次数，作为二维数组的行数。
    3、遍历字典，将每个数字添加到二维数组中。
    4、返回二维数组。
"""

from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_count = {}
        max_count = 0
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
            max_count = max(max_count, num_count[num])
        
        res = [[] for _ in range(max_count)]
        for num, count in num_count.items():
            for i in range(count):
                res[i].append(num)
        return res
    
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # 使用计数数组而不是字典（因为1 <= nums[i] <= nums.length）
        count = [0] * (len(nums) + 1)
        result = []
        
        for num in nums:
            # 如果当前数字的出现次数等于结果数组的长度，需要新增一行
            if count[num] == len(result):
                result.append([])
            # 将数字添加到对应行
            result[count[num]].append(num)
            # 更新计数
            count[num] += 1
            
        return result
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 1, 2, 3, 1]
    print(solution.findMatrix(nums))
