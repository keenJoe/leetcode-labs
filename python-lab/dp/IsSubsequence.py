# 392. Is Subsequence

'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

过程
    1、双指针
    2、dp
    3、贪心
        1、从t中找到s的第一个字符
        2、从t中找到s的第二个字符
        3、重复上述过程，直到找到s的最后一个字符
        4、如果找到s的最后一个字符，则s是t的子序列
        5、如果找不到s的最后一个字符，则s不是t的子序列
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 空字符串是任何字符串的子序列
        if len(s) == 0:
            return True
            
        # 如果s长度大于t，一定不是子序列
        if len(s) > len(t):
            return False
        
        prev_index = -1
        curr_index = -1
        
        for i in range(len(t)):
            c = t[i]
            for j in range(len(s)):
                if c == s[j]:
                    prev_index = curr_index
                    curr_index = j
                     
                    if curr_index - prev_index > 1:
                        return False
                    break
                
        if curr_index == -1:
            return False
                
        return True
    
    def isSubsequence_1(self, s: str, t: str) -> bool:
        # 空字符串是任何字符串的子序列
        if len(s) == 0:
            return True
            
        # 如果s长度大于t，一定不是子序列
        if len(s) > len(t):
            return False
        
        i = 0  # s的指针
        j = 0  # t的指针
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        # 如果i到达s的末尾，说明找到了所有字符
        return i == len(s)


if __name__ == "__main__":
    s = "aaaaaa"
    t = "bbaaaa"
    print(Solution().isSubsequence_1(s, t))