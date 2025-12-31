# 713. Subarray Product Less Than K

'''
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
 

示例 1：

输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2]、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
示例 2：

输入：nums = [1,2,3], k = 0
输出：0


1、初始化窗口的长度为 1，这个是必要条件；
2、然后计算乘积是否小于 k。如果小于，则子数组数目加 1；
3、然后右移整个窗口，继续判断下一个子数组。
4、注意：如果乘积大于等于 k，则需要移动左边界，直到乘积小于 k。
'''

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        current_product = 1
        count = 0


        for right in range(len(nums)):
            current_product *= nums[right]
            while current_product >= k:
                current_product //= nums[left]
                left += 1
            
            count += right - left + 1

        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(solution.numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3], 19))