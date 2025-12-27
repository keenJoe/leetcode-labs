# 632. Smallest Range Covering Elements from K Lists

'''
你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

 

示例 1：

输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释： 
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
示例 2：

输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]


'''


from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        merged = []
        for i, lst in enumerate(nums):
            for val in lst:
                merged.append((val, i))
        
        merged.sort()

        count = {}
        valid = 0
        k = len(nums)

        left = 0
        right = 0
        n = len(merged)
        min_range = float('inf')
        result = []
        while right < n:
            # 加入右边界，计算窗口内每个列表的元素个数
            count[merged[right][1]] = count.get(merged[right][1], 0) + 1
            if count[merged[right][1]] == 1:
                valid += 1
            while valid == k:
                if merged[right][0] - merged[left][0] < min_range:
                    min_range = merged[right][0] - merged[left][0]
                    result = [merged[left][0], merged[right][0]]
                count[merged[left][1]] -= 1
                if count[merged[left][1]] == 0:
                    valid -= 1
                left += 1
            right += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))