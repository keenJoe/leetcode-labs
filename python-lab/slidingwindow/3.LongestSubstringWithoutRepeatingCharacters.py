# 3. Longest Substring Without Repeating Characters

'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 0
        left = 0
        right = 0
        map = {}
        while right < len(s):
            if s[right] in map:
                left = max(left, map[s[right]] + 1)
            map[s[right]] = right
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
