# 131. Palindrome Partitioning

'''
    1、回溯法
        从第一个字符开始，判断是否是回文，如果是，则继续判断下一个字符，如果不是，则回溯
        终止条件：
            1、遍历完所有字符
            2、当前字符串是回文
        回溯条件：
            1、当前字符串是回文
            2、继续判断下一个字符
        
'''

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        # 判断是否是回文
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        def backtrack(s: str, start: int, path: List[str]):
            # 终止条件
            if start == len(s):
                res.append(path[:])
                return
            # 回溯条件
            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    path.append(s[start:i+1])
                    backtrack(s, i+1, path)
                    path.pop()
        
        backtrack(s, 0, [])
        return res


if __name__ == "__main__":
    s = "aab"
    solution = Solution()
    print(solution.partition(s))