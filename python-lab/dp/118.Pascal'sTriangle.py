# 118. Pascal's Triangle


"""
    1、根据给定的行数，定义一个二维数组，用于存储杨辉三角的每一行；
    2、第一行和第二行直接初始化；
    3、第一列直接初始化为1；
    4、第二列开始等于上一行的前一列和当前列的和；
"""

from typing import List

class Solution:
    # 动态规划，二维数组
    def generate1(self, numRows: int) -> List[List[int]]:
        # 初始化二维数组，每个位置都是1
        array = [[1] * i for i in range(1, numRows + 1)]
        print(array)
        
        # 填充中间的元素
        # 从第三行开始，每个位置的值等于上一行的前一列和当前列的和
        for i in range(2, numRows):
            # 从第二列开始，每个位置的值等于上一行的前一列和当前列的和
            for j in range(1, i):
                array[i][j] = array[i-1][j-1] + array[i-1][j]
        return array
    
    # 动态规划，使用一维数组进行空间优化
    # 因为每一行的元素只和上一行有关，所以可以只使用一维数组
    def generate(self, numRows: int) -> List[List[int]]:
        # 存放最后的结果
        res = []
        
        # 填充中间的元素
        for i in range(numRows):
            # 初始化当前行
            current_row = [1] * (i + 1)
            # 从第二列开始，每个位置的值等于上一行的前一列和当前列的和
            # 当 i= 0 和 i= 1 时，不需要填充中间的元素，从i=2开始才开始填充
            for j in range(1, i):
                current_row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(current_row)
        return res
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.generate1(5))