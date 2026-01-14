# 303. Range Sum Query - Immutable

'''
给定一个整数数组  nums，处理以下类型的多个查询:

计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int left, int right) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )
 

示例 1：

输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
'''

from typing import List


# class NumArray:

#     num_array: List[int] = []
#     def __init__(self, nums: List[int]):
#         self.num_array = nums

#     # 前缀和的优化点是什么呢？减少重复计算？
#     def sumRange(self, left: int, right: int) -> int:
#         return sum(self.num_array[left:right+1])

class NumArray:
    def __init__(self, nums: List[int]):
        # 构建前缀和数组，prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
        # prefix[0] = 0，这样处理边界更方便
        n = len(nums)
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # 区间和 = prefix[right+1] - prefix[left]
        # 例如：sumRange(2, 5) = prefix[6] - prefix[2]
        #     = (nums[0]+...+nums[5]) - (nums[0]+nums[1])
        #     = nums[2] + nums[3] + nums[4] + nums[5]
        return self.prefix[right + 1] - self.prefix[left]


if '__main__' == __name__:
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    print(numArray.sumRange(0, 2))
    print(numArray.sumRange(2, 5))
    print(numArray.sumRange(0, 5))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)