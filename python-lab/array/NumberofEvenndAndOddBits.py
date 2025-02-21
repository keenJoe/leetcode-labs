# 2595. Number of Even and Odd Bits

from typing import List


'''
    1、将数字转换为二进制字符串；
    2、遍历字符串，统计偶数位和奇数位的1的个数；
'''


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary_str = bin(n)[2:]  # "10"
        # 从右到左读取，需要反转字符串
        binary_str = binary_str[::-1]  
        even_count = 0
        odd_count = 0
        for i in range(len(binary_str)):
            if binary_str[i] == '1':
                if i % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
        return [even_count, odd_count]
    

class Solution:
    # 位运算
    def evenOddBit(self, n: int) -> List[int]:
        even_count = 0
        odd_count = 0
        pos = 0
        while n:
            if n & 1:  # 检查最低位是否为1
                if pos % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            n >>= 1    # 右移一位
            pos += 1
        return [even_count, odd_count]


if __name__ == "__main__":
    print(Solution().evenOddBit(2))