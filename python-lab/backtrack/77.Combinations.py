# 77. Combinations

'''
    给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
    你可以按 任何顺序 返回答案。


'''


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []
        def backtrack(start, count):
            # 剪枝：如果剩余的数字不够凑成k个 或 count大于k
            if count > k or n - start + 1 < k - count:
                return

            if count == k:
                res.append(path[:])
                return
            
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, count + 1)
                path.pop()

        backtrack(1, 0)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))
