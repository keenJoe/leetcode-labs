# 922. Sort Array By Parity II

'''
    使用双指针，一个指针遍历奇数位，一个指针遍历偶数位，如果奇数位是偶数，偶数位是奇数，则交换
'''

from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParityII([4,2,5,7]))