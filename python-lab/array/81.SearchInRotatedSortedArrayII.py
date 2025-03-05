# 81. Search in Rotated Sorted Array II

'''
    1、先找到旋转点；

    2、然后判断target在旋转点的左边还是右边；
    3、最后在左边或右边进行二分查找；
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
            
        # 找到旋转点
        pivot = self.find_pivot(nums)
        
        # 判断target在旋转点的左边还是右边
        if target >= nums[0]:
            end = pivot if pivot > 0 else len(nums)
            return self.binary_search(nums, 0, end-1, target)
        else:
            return self.binary_search(nums, pivot, len(nums)-1, target)


    # ⚠️ 这个方法只能找到旋转点，不能找到target。
    # ⚠️ 需要使用二分查找来找到target。
    # ⚠️ 二分查找是边界元素和target比较，而找旋转点是边界元素和mid比较。
    def find_pivot(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left
    
    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> bool:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.search([2,5,6,0,0,1,2], 0))
    print(s.search([2,5,6,0,0,1,2], 3))
    print(s.search([1], 1))
    print(s.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2))