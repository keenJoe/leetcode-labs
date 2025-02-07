# 118. Pascal's Triangle

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 初始化结果列表
        triangle = []
        
        for row in range(numRows):
            # 初始化当前行
            curr_row = [1] * (row + 1)
            # 填充当前行的中间元素
            for j in range(1, row):
                print(j)
                curr_row[j] = triangle[row-1][j-1] + triangle[row-1][j]
                
            triangle.append(curr_row)
        
        return triangle
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(5))