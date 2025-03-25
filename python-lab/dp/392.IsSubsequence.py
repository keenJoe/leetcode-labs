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

from functools import lru_cache


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
    
    # 双指针，这个方法应该是最容易理解的答案
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
    
    # 递归
    def isSubsequence_2(self, s: str, t: str) -> bool:
        def recursive(i, j):
            # 基础情况：s已经匹配完
            if i == len(s):
                return True
            # 基础情况：t已经用完但s还没匹配完
            if j == len(t):
                return False
            
            # 如果当前字符匹配
            if s[i] == t[j]:
                return recursive(i + 1, j + 1)
            # 当前字符不匹配，在t中继续寻找
            return recursive(i, j + 1)
        
        return recursive(0, 0)
    

    def isSubsequence(self, s: str, t: str) -> bool:
        return self.dfs(s, t, 0, 0)

    def dfs(self, s: str, t: str, i: int, j: int) -> bool:
        if i == len(s):
            return True
        if j == len(t):
            return False
        
        if s[i] == t[j]:
            return self.dfs(s, t, i + 1, j + 1)
        else:
            return self.dfs(s, t, i, j + 1)
        
    # 从后向前填充dp数组，从递归改成dp
    def isSubsequence_4(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        
        # dp[i][j] 表示 s[i:] 是否是 t[j:] 的子序列
        dp = [[False] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        # 空字符串是任何字符串的子序列
        dp[len(s)][len(t)] = True
        
        # 初始化最后一列
        for i in range(len(s)):
            dp[i][len(t)] = False
        
        # 初始化最后一行
        for j in range(len(t)):
            dp[len(s)][j] = True
        
        # 从后向前填充dp数组
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
        
        return dp[0][0]
    
    def isSubsequence_5(self, s: str, t: str) -> bool:
        # 特殊情况：空字符串
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        
        # dp[i][j] 表示 s[i:] 是否是 t[j:] 的子序列
        # 现在只考虑非空字符串的情况
        dp = [[False] * len(t) for _ in range(len(s))]
        
        # 初始化第一行：s的第一个字符和t的每个字符比较
        for j in range(len(t)):
            if s[0] == t[j]:
                dp[0][j] = True
            elif j > 0:
                dp[0][j] = dp[0][j-1]
        
        # 填充其余部分
        for i in range(1, len(s)):
            for j in range(i, len(t)):
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1]
                elif j > 0:
                    dp[i][j] = dp[i][j-1]
        
        return dp[len(s)-1][len(t)-1]

    
    def isSubsequence(self, s: str, t: str) -> bool:
        @lru_cache(None)  # 使用Python的内置缓存装饰器
        def recursive(i, j):
            # 基础情况
            if i == len(s):
                return True
            if j == len(t):
                return False
            
            # 如果当前字符匹配
            if s[i] == t[j]:
                return recursive(i + 1, j + 1)
            # 不匹配则跳过t中的当前字符
            return recursive(i, j + 1)
        
        return recursive(0, 0)
    
    # 手动实现记忆化版本
    def isSubsequence2(self, s: str, t: str) -> bool:
        memo = {}  # 记忆化字典
        
        def recursive(i, j):
            # 检查是否已经计算过
            if (i, j) in memo:
                return memo[(i, j)]
            
            # 基础情况
            if i == len(s):
                return True
            if j == len(t):
                return False
            
            # 计算结果
            if s[i] == t[j]:
                result = recursive(i + 1, j + 1)
            else:
                result = recursive(i, j + 1)
            
            # 存储结果
            memo[(i, j)] = result
            return result
        
        return recursive(0, 0)
    
    # 带打印的递归版本（用于理解过程）
    def isSubsequence3(self, s: str, t: str) -> bool:
        def recursive(i, j, indent=0):
            # 打印当前状态
            print(" " * indent + f"检查 s[{i}:] 和 t[{j}:]")
            
            # 基础情况
            if i == len(s):
                print(" " * indent + "s匹配完成，返回True")
                return True
            if j == len(t):
                print(" " * indent + "t用完了，s还没匹配完，返回False")
                return False
            
            # 当前字符匹配
            if s[i] == t[j]:
                print(" " * indent + f"匹配: s[{i}]={s[i]} == t[{j}]={t[j]}")
                return recursive(i + 1, j + 1, indent + 2)
            
            # 当前字符不匹配
            print(" " * indent + f"不匹配: s[{i}]={s[i]} != t[{j}]={t[j]}")
            return recursive(i, j + 1, indent + 2)
        
        return recursive(0, 0)
    
    # 动态规划
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        
        # 创建DP数组，dp[i][j]表示s的前i个字符是否是t的前j个字符的子序列
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # 初始化：空字符串是任何字符串的子序列
        for j in range(n + 1):
            dp[0][j] = True
            
        # 填充DP数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    # 如果当前字符相同，则看前面的子问题
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 如果当前字符不同，则看t的前j-1个字符
                    dp[i][j] = dp[i][j-1]
        
        return dp[m][n]
    
    # 空间优化版本
    def isSubsequence2(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        
        # 只需要保存上一行的状态
        dp = [True] + [False] * m
        
        for j in range(n):
            # 保存上一个状态（左上角的值）
            prev = dp[0]  # 空字符串永远是子序列
            for i in range(1, m + 1):
                temp = dp[i]  # 保存当前值供下一次使用
                if s[i-1] == t[j]:
                    dp[i] = prev
                else:
                    dp[i] = dp[i]  # 保持不变
                prev = temp  # 更新左上角的值
        
        return dp[m]

    # 进阶：处理多个s的查询
    def isSubsequence3(self, s: str, t: str) -> bool:
        # 预处理：记录t中每个字符出现的位置
        char_indices = {}
        for i, char in enumerate(t):
            char_indices.setdefault(char, []).append(i)
        
        # 当前需要匹配的位置
        curr_pos = 0
        
        # 检查s中的每个字符
        for char in s:
            # 如果字符不在t中，直接返回False
            if char not in char_indices:
                return False
            
            # 二分查找大于curr_pos的最小位置
            indices = char_indices[char]
            pos = self.binary_search(indices, curr_pos)
            
            # 如果找不到合适的位置，返回False
            if pos == len(indices):
                return False
            
            # 更新当前位置
            curr_pos = indices[pos] + 1
        
        return True
    
    def binary_search(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    s = "aaaaaa"
    t = "bbaaaa"
    print(Solution().isSubsequence_1(s, t))