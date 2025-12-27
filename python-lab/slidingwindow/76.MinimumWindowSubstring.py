# 76. Minimum Window Substring

'''
给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。

测试用例保证答案唯一。

 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。

其实就是判断t中的每个字符是否都在s中出现，如果出现，则返回s中出现t中字符的最短子串

从左向右开始移动窗口
从第三个字符开始移动窗口，直到窗口内包含t中的所有字符
如果当前子串包含t中的所有字符，则记录当前子串的长度，并更新最小长度
如果当前子串不包含t中的所有字符，则继续移动窗口
直到窗口右移到末尾时，返回最小长度
'''

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         left = 0
#         right = 0
#         min_length = len(s)
#         min_window = ""

#         for right in range(2, len(s)) or left <= right:
#             window = s[left:right+1]
#             print(window)
#             if all(t[i] in window for i in range(len(t))):
#                 if len(window) < min_length:
#                     min_length = len(window)
#                     min_window = window
#                 left += 1
#             elif right == len(s) - 1:
#                 left += 1

#         return min_window

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # t 中每个字符的需求量
        need = Counter(t)
        # 窗口中的字符计数
        window = {}
        
        left = 0
        # 已满足的字符种类数
        valid = 0
        # 需要满足的字符种类数
        required = len(need)
        
        min_len = float('inf')
        min_start = 0
        
        for right in range(len(s)):
            # 扩展右边界
            c = s[right]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            # 当窗口满足条件时，收缩左边界
            while valid == required:
                # 更新最小窗口
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                # 收缩左边界
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]
        
        


if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solution.minWindow(s, t))