# 89. Gray Code

'''
    1、先确定最大值的二进制；
    2、然后从0开始选择，选择一个数，使得它与上一个数的二进制只有一位不同；
    3、重复2，直到找到所有可能的数；
    4、返回结果；

'''

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        max_num = 2 ** n

        binary = []
        for i in range(max_num):
            binary.append(i ^ (i >> 1))
        return binary

if __name__ == "__main__":
    # s = Solution()
    # print(s.grayCode(2))

    max_num = 2 ** 2
    print(max_num)
    # 转二进制
    binary = bin(max_num)
    print(binary)

    # 转字符串
    binary_str = str(binary)
    # 只保留数字
    binary_str = binary_str[2:]
    print(binary_str)

    binary = []
    for i in range(max_num):
        binary.append(i ^ (i >> 1))
    print(binary)


    
    
