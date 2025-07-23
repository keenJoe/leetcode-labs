# 14. Longest Common Prefix

'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

1、选取长度最短的字符串，作为公共前缀
2、遍历其他字符串，如果公共前缀等于当前字符串，则返回公共前缀
3、如果公共前缀不等于当前字符串，则公共前缀长度减一，继续遍历
4、如果公共前缀长度为0，则返回空字符串

公共前缀不是相同的子串，必须从第一个字符开始比较。

公共前缀的定义：
1、必须从索引0开始
2、所有字符串的开头部分完全相同
3、连续且从头开始

开始没有理解公共前缀的定义，导致自己的实现思路不正确。

'''


from typing import List


class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        # 选取第一个字符串作为公共前缀
        for i in range(len(strs[0])):
            # 遍历其他字符串，开始进行比较
            for j in range(1, len(strs)):
                # 如果当前字符串的长度小于公共前缀的长度，或者当前字符串的第 i 个字符不等于公共前缀的第 i 个字符，则返回公共前缀的第 i 个字符之前的部分
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        # 如果遍历完所有字符串，则返回公共前缀
        return strs[0]
    

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # 空数组处理
            return ""
        
        # 找到最短字符串长度，避免越界
        min_len = min(len(s) for s in strs)
        
        for i in range(min_len):
            char = strs[0][i]  # 当前比较的字符
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return strs[0][:i]
        
        print(min_len)
        return strs[0][:min_len]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["ilower", "flow", "flight"]))  # "fl"
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))  # ""
    print(solution.longestCommonPrefix(["ab", "a"]))  # "a"