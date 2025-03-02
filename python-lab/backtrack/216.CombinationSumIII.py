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
    
    # 剪枝优化
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 特判：快速处理无效情况
        if k <= 0 or n <= 0 or k > 9 or n > 45:  # 45是1-9的和
            return []
        if k == 9 and n != 45:  # 如果需要9个数，和只能是45
            return []
        
        res = []
        path = []
        
        def backtrack(start: int, remain: int, count: int):
            # 剪枝：剩余数字不够凑成k个 或 remain小于0
            if remain < 0 or count > k:
                return
            # 找到符合条件的组合
            if count == k and remain == 0:
                res.append(path[:])
                return
                
            # 优化搜索范围：考虑剩余需要的数字个数
            # 确保剩余的数字足够多，且不会超过9
            remain_count = k - count
            if 10 - start < remain_count:
                return
                
            for i in range(start, min(remain + 1, 10)):
                # 剪枝：如果剩余的数全取最大值也不够，或全取最小值也太大，直接返回
                max_possible = (19 - remain_count + i) * remain_count // 2
                min_possible = (i + i + remain_count - 1) * remain_count // 2
                if remain > max_possible or remain < min_possible:
                    break
                    
                path.append(i)
                backtrack(i + 1, remain - i, count + 1)
                path.pop()
        
        backtrack(1, n, 0)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
    print(s.combinationSum3(4, 1))
    print(s.combinationSum3(3, 2))
    print(s.combinationSum3(9, 45))