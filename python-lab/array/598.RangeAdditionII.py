# 598. Range Addition II

from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
    
        min_row = min(op[0] for op in ops)
        min_col = min(op[1] for op in ops)
        
        return min_row * min_col
        
        
    
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxCount(3, 3, [[2, 2], [3, 3]]))
