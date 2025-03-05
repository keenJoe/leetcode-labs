# 81. Search in Rotated Sorted Array II

'''
    1、先判断mid和target的大小关系；
    2、如果mid和target相等，则返回True；
    3、如果mid和target不等，处理边界值；
        （1）如果mid和target不等，且nums[l] <= nums[mid]，则说明左半部分有序；
        （2）如果nums[l] <= target and target < nums[mid]，则说明target在左半部分，则将右边界缩小到mid-1；
        （3）否则，说明target在右半部分，则将左边界缩小到mid+1；
        
        （4）如果mid和target不等，且nums[l] > nums[mid]，则说明右半部分有序；
        （5）如果nums[mid] < target and target <= nums[n - 1]，则说明target在右半部分，则将左边界缩小到mid+1；
        （6）否则，说明target在左半部分，则将右边界缩小到mid-1；
    10、最后返回False；
    
    在3中确定哪一部分有序非常重要。
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        n = len(nums)
        if n == 1:
            return nums[0] == target
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            
            # 处理左中右三个位置的值都相同的特殊情况
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                # 目标值在左半有序部分，这种情况下，左侧一定有序
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False
    
    
    def search_1(self, nums: List[int], target: int) -> bool:
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