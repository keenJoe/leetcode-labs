# 119. Pascal's Triangle II

from typing import List

class Solution:
    # 动态规划，空间优化，直接存储当前行
    def getRow(self, rowIndex: int) -> List[int]:
        # 初始化结果列表
        triangle = [1] * (rowIndex + 1)
        
        for i in range(1, rowIndex + 1):
            # 从后向前遍历更新当前行
            for j in range(i - 1, 0, -1):
                triangle[j] = triangle[j] + triangle[j - 1]
        
        return triangle

    # 动态规划，使用一维数组存储当前行，并更新上一行
    def getRow_old_2(self, rowIndex: int) -> List[int]:
        # 初始化结果列表
        triangle = [1] * (rowIndex + 1)
        
        for row in range(rowIndex + 1):
            # 初始化当前行
            curr_row = [1] * (row + 1)
            # 填充当前行的中间元素
            prev =1
            for j in range(1, row):
                curr_row[j] = prev + triangle[j]
                prev = triangle[j]
                
            triangle = curr_row
        
        return triangle
    
    # 动态规划，使用二维数组存储所有元素，最后返回最后一行
    def getRow_old(self, rowIndex: int) -> List[int]:
        # 初始化结果列表
        triangle = []
        
        for row in range(rowIndex + 1):
            # 初始化当前行
            curr_row = [1] * (row + 1)
            # 填充当前行的中间元素
            for j in range(1, row):
                curr_row[j] = triangle[row-1][j-1] + triangle[row-1][j]
                
            triangle.append(curr_row)
        
        return triangle[rowIndex]

if __name__ == "__main__":
    solution = Solution()
    print(solution.getRow(3))
    # i = 2
    # for j in range(i - 1, 0, -1):
    #     print(j)
    # print("当前遍历的：{}".format(i))