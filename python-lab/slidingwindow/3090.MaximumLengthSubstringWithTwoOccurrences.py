# 3090. Maximum Length Substring With Two Occurrences

'''
给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该子字符串的 最大 长度。

 

示例 1：

输入： s = "bcbbbcba"

输出： 4

解释：

以下子字符串长度为 4，并且每个字符最多出现两次："bcbbbcba"。

示例 2：

输入： s = "aaaa"

输出： 2

解释：

以下子字符串长度为 2，并且每个字符最多出现两次："aaaa"。


需要哈希表存储出现过的字符和次数
如果有字符出现的次数超过两次，那么就需要移动左指针到该字符第一次出现的位置的下一个位置
然后计算当前窗口的长度，并更新最大长度
然后继续移动右指针，直到窗口内每个字符出现次数都小于等于2
'''

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        count = {}
        left, right = 0, 0
        max_length = 0

        while right < len(s):
            if s[right] in count:
                if count[s[right]] == 2:
                    while s[left] != s[right]:
                        count[s[left]] -= 1
                        left += 1
                    # count[s[left]] -= 1
                    left += 1
                else:
                    count[s[right]] += 1
            else:
                count[s[right]] = 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLengthSubstring("abacabad"))