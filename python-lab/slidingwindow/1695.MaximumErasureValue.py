# 1695. Maximum Erasure Value

'''
给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。

返回 只删除一个 子数组可获得的 最大得分 。

如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

 

示例 1：

输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]
示例 2：

输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]

'''


from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        left = 0
        count = {}

        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1

            # 判断是否重复，如果重复，则需要删除左边的元素
            if count[nums[right]] > 1:
                while nums[left] != nums[right]:
                    count[nums[left]] -= 1
                    left += 1
                count[nums[left]] -= 1
                left += 1
            
            max_score = max(max_score, sum(nums[left:right+1]))
        return max_score


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumUniqueSubarray([4,2,4,5,6]))
    print(solution.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))