# 2643. Row With Maximum Ones

from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        max_row = 0
        max_count = 0
        for i in range(m):
            count = sum(mat[i])
            if count > max_count:
                max_count = count
                max_row = i
        return [max_row, max_count]
            

if __name__ == "__main__":
    s = Solution()
    mat = [[0, 1], [1, 0]]
    print(s.rowAndMaximumOnes(mat))
