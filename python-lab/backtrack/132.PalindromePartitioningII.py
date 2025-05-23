# 132. Palindrome Partitioning II

'''
   将整个字符串分割成若干个子字符串，使每个子字符串都是回文，并且子字符串的数量最少。
   返回最少分割次数。
   终止条件：
        1、遍历完整个字符串，且分割后的子字符串都是回文
        2、path中子字符串的整个长度等于s的长度
   回溯条件：
        
        
'''

from typing import List


class Solution:
    # def minCut(self, s: str) -> int:
    #     res = []
    #     def is_palindrome(s: str) -> bool:
    #         return s == s[::-1]
        
    #     def backtrack(s: str, start: int, path: List[str]):
    #         if start == len(s):
    #             res.append(path[:])
                
    #             return
            
    #         for i in range(start, len(s)):
    #             k = -1
    #             for j in range(i, len(s)):
    #                 if is_palindrome(s[start:j + 1]):
    #                     print(f"s[start:j]: {s[start:j + 1]}")
    #                     k = j
    #                 else:
    #                     break
    #             # print(f"k: {k}")
    #             # print(f"s[start:k]: {s[start:k]}")
    #             print("===============")
    #             if k != -1:
    #                 path.append(s[start:k + 1])
    #                 backtrack(s, k + 1, path)
    #                 path.pop()
                    
                    
            
    #     backtrack(s, 0, [])
    #     # print(res)
    #     return len(res) - 1 if len(res) > 0 else 0
    def minCut(self, s: str) -> int:
        # 记录最小切割次数
        min_cuts = float('inf')
        
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        def backtrack(s: str, start: int, path: List[str]):
            nonlocal min_cuts
            
            # 已经到达字符串末尾
            if start == len(s):
                # 更新最小切割次数（切割次数 = 段数 - 1）
                min_cuts = min(min_cuts, len(path) - 1)
                return
            
            # 直接尝试每个可能的切割点
            for i in range(start, len(s)):
                # 如果当前子串是回文
                if is_palindrome(s[start:i + 1]):
                    path.append(s[start:i + 1])
                    backtrack(s, i + 1, path)
                    path.pop()
        
        backtrack(s, 0, [])
        return min_cuts
    
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # 预处理回文信息
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for i in range(n-1):
            is_pal[i][i+1] = (s[i] == s[i+1])
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                is_pal[i][j] = (s[i] == s[j]) and is_pal[i+1][j-1]
        
        # dp[i]表示s[0:i]的最小切割次数
        dp = [i for i in range(-1, n)]
        
        for i in range(1, n+1):
            for j in range(i):
                if is_pal[j][i-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n]


if __name__ == "__main__":
    s = "aabac"
    solution = Solution()
    print(solution.minCut(s))