# 66. Plus One

'''
加一的问题主要是进位问题，从后往前遍历。
如果当前位是9，则进位，当前位为0。然后继续遍历前一位。
如果不是 9 直接加一，然后返回；
如果遍历结束，说明最高位是9，则需要进位，在最高位插入1。
'''

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits = []
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                if digits[i] == 9:
                    new_digits.append(0)
                    carry = 1
                else:
                    new_digits.append(digits[i] + 1)
                    carry = 0
            else:
                if digits[i] == 9 and carry == 1:
                    new_digits.append(0)
                    carry = 1
                else:
                    new_digits.append(digits[i] + carry)
                    carry = 0
        if carry:
            new_digits.append(1)
        return new_digits[::-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))
    print(solution.plusOne([4, 3, 2, 1]))
    print(solution.plusOne([9]))
    print(solution.plusOne([9, 9, 9]))
    print(solution.plusOne([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))