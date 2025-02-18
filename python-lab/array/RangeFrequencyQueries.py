# 2080. Range Frequency Queries

from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.arr = arr  # 存储输入数组

    def query(self, left: int, right: int, value: int) -> int:
        # 计算在区间[left, right]内值为value的元素个数
        count = 0
        for i in range(left, right + 1):
            if self.arr[i] == value:
                count += 1
        return count
    

class RangeFreqQuery1:
    def __init__(self, arr: List[int]):
        # 使用defaultdict存储每个数字出现的位置索引
        self.positions = defaultdict(list)
        for i, num in enumerate(arr):
            self.positions[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        # 使用二分查找找到区间[left, right]内value的出现次数
        pos_list = self.positions[value]
        # 找到第一个大于等于left的位置
        left_pos = bisect_left(pos_list, left)
        # 找到第一个大于right的位置
        right_pos = bisect_right(pos_list, right)
        return right_pos - left_pos
    
class RangeFreqQuery2:
    def __init__(self, arr: List[int]):
        # 使用defaultdict存储每个数字出现的位置索引
        self.positions = defaultdict(list)
        for i, num in enumerate(arr):
            self.positions[num].append(i)
    
    def binary_search_left(self, nums: List[int], target: int) -> int:
        # 查找第一个大于等于target的位置
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
    
    def binary_search_right(self, nums: List[int], target: int) -> int:
        # 查找第一个大于target的位置
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

    def query(self, left: int, right: int, value: int) -> int:
        pos_list = self.positions[value]
        # 使用自定义二分查找替代bisect
        left_pos = self.binary_search_left(pos_list, left)
        right_pos = self.binary_search_right(pos_list, right)
        return right_pos - left_pos


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)