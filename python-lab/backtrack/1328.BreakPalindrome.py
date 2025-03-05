# 1328. Break a Palindrome

'''
    1、如果字符串长度为1，直接返回空字符串；
    2、要满足两个条件：
        1、不是回文串；
        2、替换的后的字典序最小；
    3、遍历字符串
        1、如果当前字符为‘a’，则可以替换为‘b’，然后验证是否为回文串；
            1、如果替换后为回文串，保留；
            2、如果替换后不是回文串，则继续遍历；
        2、如果当前字符为其他字符，则可以替换为‘a’，然后验证是否为回文串；
            1、如果替换后为回文串，保留；
            2、如果替换后不是回文串，则继续遍历；
        3、最后返回最小的字典序的回文串；
'''

class Solution:
    def breakPalindrome1(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        res = []
        for i in range(len(palindrome)):
            if palindrome[i] == 'a' and i == 0:
                str = 'b' + palindrome[1:]
                if str != str[::-1]:
                    res.append(str)
            else:
                if palindrome[i] != 'a':
                    str = palindrome[:i] + 'a' + palindrome[i+1:]
                    if str != str[::-1]:
                        res.append(str)
                else:
                    str = palindrome[:i] + 'b' + palindrome[i+1:]
                    if str != str[::-1]:
                        res.append(str)
        return min(res)
    
    def breakPalindrome(self, palindrome: str) -> str:
        # 特判：长度为1的字符串无法破坏回文性质
        if len(palindrome) <= 1:
            return ""
            
        n = len(palindrome) // 2
        print(n)
        # 只需要遍历前半部分
        for i in range(n):
            print(i)
            # 如果当前字符不是'a'，改成'a'一定是最小的解
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        # 如果前半部分都是'a'，把最后一个字符改成'b'
        return palindrome[:-1] + 'b'

if __name__ == "__main__":
    s = Solution()
    print(s.breakPalindrome("abccba"))
    print(s.breakPalindrome("a"))
    print(s.breakPalindrome("aa"))
    print(s.breakPalindrome("aba"))