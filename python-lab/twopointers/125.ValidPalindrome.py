# 125. Valid Palindrome

"""
1、双指针
    先要去除字符串中的非字母和数字字符
    然后使用双指针，一个从前往后，一个从后往前，比较两个指针指向的字符是否相同
    如果相同，则继续移动指针，直到两个指针相遇
    如果不同，则返回False
    如果两个指针相遇，则返回True
2、栈
    先要去除字符串中的非字母和数字字符
    计算字符串的长度
    如果长度为奇数，则中间的字符不参与比较
    如果长度为偶数，则中间两个字符参与比较
    使用栈来存储字符串前半部分的字符
    然后从栈中弹出字符，与字符串后半部分的字符进行比较
    如果相同，则继续弹出字符，直到栈为空
    如果不同，则返回False
    如果栈为空，则返回True
3、递归
4、动态规划
"""

import re

class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    

    def isPalindrome_stack(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        
        stack = []
        length = len(s)
        for i in range(length // 2):
            stack.append(s[i])
        if length % 2 == 0:
            start = length // 2
        else:
            start = length // 2 + 1
        
        for i in range(start, length):
            if s[i] != stack.pop():
                return False
        return True
    

    def isPalindrome_recursive(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        
        def recursive(s, left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return recursive(s, left + 1, right - 1)
        return recursive(s, 0, len(s) - 1)


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))