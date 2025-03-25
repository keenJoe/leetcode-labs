# 2711. Difference of Number of Distinct Values on Diagonals

from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s1 = set()
                x, y = i + 1, j + 1
                while x < m and y < n:
                    s1.add(grid[x][y])
                    x += 1
                    y += 1
                s2 = set()
                x, y = i - 1, j - 1
                while x >= 0 and y >= 0:
                    s2.add(grid[x][y])
                    x -= 1
                    y -= 1
                res[i][j] = abs(len(s1) - len(s2))
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.differenceOfDistinctValues([[1,2,3],[4,5,6],[7,8,9]]))
    print(solution.differenceOfDistinctValues([[1,1,1],[1,1,1],[1,1,1]]))
    