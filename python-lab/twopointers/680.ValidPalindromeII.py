# 680. Valid Palindrome II

'''
    使用双指针，从两端向中间移动，如果遇到不相同的字符，则有两种情况：
    1. 删除左指针指向的字符，检查剩余字符串是否为回文
    2. 删除右指针指向的字符，检查剩余字符串是否为回文
    
    使用递归，如果两端字符相同，则继续移动指针，如果不同，则分别检查删除左指针或右指针指向的字符后的字符串是否为回文
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True
    
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.validPalindrome("a"))
