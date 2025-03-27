# 2712. Minimum Cost to Make All Characters Equal

class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        total_cost = 0
        
        # 遍历除最后一个字符外的所有字符
        for i in range(n - 1):
            # 如果相邻字符不同，计算最小翻转成本
            if s[i] != s[i + 1]:
                # 在位置i处进行分割，选择成本较小的一侧翻转
                flip_cost = min(i + 1, n - (i + 1))
                total_cost += flip_cost
        
        return total_cost

def test_solution():
    solution = Solution()
    assert solution.minimumCost("010101") == 6
    assert solution.minimumCost("1111") == 0