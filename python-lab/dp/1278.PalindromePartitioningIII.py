# 1278. Palindrome Partitioning III

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        
        # 计算将子串s[i:j+1]变成回文串需要修改的最少字符数
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    cost[i][j] = cost[i+1][j-1] if i+1 <= j-1 else 0
                else:
                    cost[i][j] = cost[i+1][j-1] + 1 if i+1 <= j-1 else 1
        
        # dp[i][j]表示将s[0:i+1]分割成j+1个子串所需的最小修改次数
        dp = [[float('inf')] * k for _ in range(n)]
        
        # 初始化：将整个字符串s[0:i+1]作为一个子串的情况
        for i in range(n):
            dp[i][0] = cost[0][i]
        
        # 动态规划填表
        for i in range(n):
            for j in range(1, min(i + 1, k)):
                for m in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], dp[m][j-1] + cost[m+1][i])
        
        return dp[n-1][k-1]


if __name__ == "__main__":
    s = "abc"
    k = 2
    print(Solution().palindromePartition(s, k))
