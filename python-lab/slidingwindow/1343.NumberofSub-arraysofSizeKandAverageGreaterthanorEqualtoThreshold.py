# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

'''
给你一个整数数组 arr 和两个整数 k 和 threshold 。

请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。


1、初始化窗口的长度为 k，这个是必要条件；
2、然后计算平均值是否大于 threshold。如果大于，则子数组数目加 1；
3、然后右移整个窗口，继续判断下一个子数组。
 

示例 1：

输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
示例 2：

输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出：6
解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
'''

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        length = len(arr)
        if length < k:
            return 0

        threshold_sum = threshold * k

        # current_sum = 0
        # for i in range(k):
        #     current_sum += arr[i]

        # count = 0
        # if current_sum >= threshold_sum:
        #     count += 1
        current_sum = sum(arr[:k])  # 使用内置sum函数
        count = 1 if current_sum >= threshold_sum else 0

        for i in range(k, length):
            current_sum += arr[i] - arr[i - k]
            if current_sum >= threshold_sum:
                count += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    print(solution.numOfSubarrays(arr, k, threshold))

    arr = [1, 1, 1, 1, 1]
    k = 1
    threshold = 0
    print(solution.numOfSubarrays(arr, k, threshold))

    arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
    k = 3
    threshold = 5
    print(solution.numOfSubarrays(arr, k, threshold))
    
    