# 1137. N-th Tribonacci Number

"""
    泰波那契序列 Tn 定义如下： 

    T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
    
    给定 n，请返回第 n 个泰波那契数 Tn 的值。
    
    示例 1：
    输入：n = 4
    输出：4
    解释：
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4

    tn = tn-1 + tn-2 + tn-3
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.tribonacci(4))
    print(solution.tribonacci(25))
