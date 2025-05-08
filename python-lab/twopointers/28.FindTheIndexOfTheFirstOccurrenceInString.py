# 28. Find the Index of the First Occurrence in a String


"""
示例 1：

输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
示例 2：

输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。

先找到needle在haystack中出现的第一个位置，然后开始比较，知道needle的最后一个字符，如果匹配，则返回needle在haystack中出现的第一个位置，否则返回-1

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        # 如果最后剩余的元素小于needle的长度， 则直接返回-1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    haystack = "hello"
    needle = "ll"
    print(solution.strStr(haystack, needle)) 