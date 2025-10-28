# 2090. K Radius Subarray Averages

'''
从第 k 位置开始计算。
如果小于 k ，则对应位置的值为 -1；
如果大于 length - k，则对应的位置值为 -1；

半径为 k，则整个窗口的长度是 2k + 1；
计算窗口内的平均值，然后赋值给对应位置；



遍历数组
如果 0 <= i - k  <= length - 1，则当前 i 是一个有效的位置，可以计算平均值，赋值给对应位置；
如果 i - k < 0 或 i + k > length - 1，则对应位置的值为 -1；
'''

from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        averages = [-1] * length
        prev = 0
        for i in range(length):
            if i - k < 0 or i + k > length - 1:
                averages[i] = -1
            else:
                if prev == 0:
                    prev = sum(nums[i-k:i+k+1])
                else:
                    prev = prev - nums[i-k-1] + nums[i+k]
                averages[i] = prev // (2*k + 1)
        return averages


if __name__ == "__main__":
    solution = Solution()
    nums = [7,4,3,9,1,8,5,2,6]
    k = 3
    print(solution.getAverages(nums, k))