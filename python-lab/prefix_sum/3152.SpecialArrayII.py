# 3152. Special Array II

'''
如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 特殊数组 。

你有一个整数数组 nums 和一个二维整数矩阵 queries，对于 queries[i] = [fromi, toi]，请你帮助你检查 子数组 nums[fromi..toi] 是不是一个 特殊数组 。

返回布尔数组 answer，如果 nums[fromi..toi] 是特殊数组，则 answer[i] 为 true ，否则，answer[i] 为 false 。

 

示例 1：

输入：nums = [3,4,1,2,6], queries = [[0,4]]

输出：[false]

解释：

子数组是 [3,4,1,2,6]。2 和 6 都是偶数。

示例 2：

输入：nums = [4,3,1,6], queries = [[0,2],[2,3]]

输出：[false,true]

解释：

子数组是 [4,3,1]。3 和 1 都是奇数。因此这个查询的答案是 false。
子数组是 [1,6]。只有一对：(1,6)，且包含了奇偶性不同的数字。因此这个查询的答案是 true。


还是要先构建前缀和数组，但是和以往构建的数组不同之处在于，这次我们需要构建两个前缀和数组，分别记录奇数和偶数的个数。
第一个前缀和数组 odd 用于记录从数组开头到当前位置为止奇数的个数，第二个前缀和数组 even 用于记录从数组开头到当前位置为止偶数的个数。
在处理每个查询时，我们可以通过前缀和数组快速计算出子数组中奇数和偶数的个数。如果子数组中奇数和偶数的个数都大于零，则说明子数组是特殊数组，返回 true；否则，返回 false

这个方案明显是错误的，即使子数组的奇数和偶数大于零，但是如果它们紧邻，那么就不是特殊数组。

当前位置的前缀和 = 当前位置前一个位置的前缀和 and （当前位置和前一个位置的奇偶性不同 = true， 否则是 false）
'''

from typing import List


class Solution:
    # def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    #     n = len(nums)
    #     prefix_special : List[bool] = [False] * n
    #     prefix_special[0] = True  # 单个元素的子数组总是特殊
    #     for i in range(1, n):
    #         prefix_special[i] = prefix_special[i - 1] and ((nums[i] ^ nums[i - 1]) & 1) == 1
        
    #     result : List[bool] = []
    #     for L, R in queries:
    #         if L == R:
    #             result.append(True)
    #         else:
    #             result.append(prefix_special[R] and (L == 0 or prefix_special[L - 1]))

    #     return result
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        # prefix[i] 表示 [0..i] 范围内"坏对"（相邻元素奇偶性相同）的数量
        prefix = [0] * n
        for i in range(1, n):
            # 如果 nums[i] 和 nums[i-1] 奇偶性相同，则是一个"坏对"
            prefix[i] = prefix[i - 1] + (1 if ((nums[i] ^ nums[i - 1]) & 1) == 0 else 0)
        
        result : List[bool] = []
        for L, R in queries:
            # 检查 [L, R] 范围内是否有"坏对"
            # 坏对的数量 = prefix[R] - prefix[L]
            bad_pairs = prefix[R] - prefix[L]
            result.append(bad_pairs == 0)
        
        return result


if __name__ == "__main__":
    solution = Solution()
    # Example test cases
    print(solution.isArraySpecial([1, 2, 3, 4, 5], [[1, 3], [0, 4]]))  # Expected output: [True, False]
    print(solution.isArraySpecial([5, 5, 5, 5], [[2, 2], [1, 3]]))      # Expected output: [True, True]

