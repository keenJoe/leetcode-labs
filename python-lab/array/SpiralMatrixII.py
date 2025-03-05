# 59. Spiral Matrix II

from typing import List

'''
    1、初始化一个n*n的矩阵
    2、从左上角开始，按照顺时针方向填充数字
    3、每次填充一个数字后，更新矩阵的边界
        1、初始化四个边界：top, bottom, left, right
    4、重复步骤2和3，直到矩阵被完全填充
'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 初始化一个n*n的矩阵
        matrix = [[0] * n for _ in range(n)]
        # 初始化四个边界
        top, bottom, left, right = 0, n - 1, 0, n - 1
        # 初始化数字
        num = 1
        # 重复步骤2和3，直到矩阵被完全填充
        while top <= bottom and left <= right:
            # 从左到右填充上边
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            # 从上到下填充右边
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            # 从右到左填充下边
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            # 从下到上填充左边
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix
    
    
    # def generateMatrix(self, n: int) -> List[List[int]]:
    #     matrix = [[0] * n for _ in range(n)]
    #     top, bottom, left, right = 0, n - 1, 0, n - 1
    #     num = 1
        
    #     while top <= bottom and left <= right:
    #         # 从左到右填充上边，top不变，增加
    #         for i in range(left, right + 1):
    #             matrix[top][i] = num
    #             num += 1
    #         top += 1
        
    #         # 从上到下填充右边，right不变，遍历top到bottom
    #         for i in range(top, bottom + 1):
    #             matrix[i][right] = num
    #             num += 1
    #         right -= 1
            
    #         # 从右到左填充下边，bottom不变，遍历right到left
    #         for i in range(right, left -1 ,-1):
    #             matrix[bottom][i] = num
    #             num += 1
    #         bottom -= 1
            
    #         # 从下到上填充左边，left不变，遍历bottom到top
    #         for i in range(bottom, top - 1, -1):
    #             matrix[i][left] = num
    #             num += 1
    #         left += 1
        
    #     return matrix


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateMatrix(3))