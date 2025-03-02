# 216. Combination Sum III


'''
    找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
    k个数字相加等于n
    只使用数字1到9
    每个数字只能使用一次
    终止条件：
        路径的长度为k
        路径的和为n
    回溯条件：
        路径的长度小于k
        路径的和小于n
'''


from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        res = []
        def backtrack(start, target):
            if len(path) == k and sum(path) == n:
                res.append(path[:])
                return
            
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, target - i)
                path.pop()

        backtrack(1, n)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
    print(s.combinationSum3(4, 1))
    print(s.combinationSum3(3, 2))
    print(s.combinationSum3(9, 45))