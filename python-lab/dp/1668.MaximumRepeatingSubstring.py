# 1668. Maximum Repeating Substring

"""
给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为 k 。单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence 的子串，那么重复值 k 为 0 。

给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。

 

示例 1：

输入：sequence = "ababc", word = "ab"
输出：2
解释："abab" 是 "ababc" 的子字符串。
示例 2：

输入：sequence = "ababc", word = "ba"
输出：1
解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
示例 3：

输入：sequence = "ababc", word = "ac"
输出：0
解释："ac" 不是 "ababc" 的子字符串。
"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # 方法1：直接构建并检查
        def check_repeating(k: int) -> bool:
            # 构建word重复k次的字符串
            repeated = word * k
            # 检查是否是sequence的子串
            return repeated in sequence
        
        # 获取可能的最大重复次数
        max_possible = len(sequence) // len(word)
        
        # 二分查找最大重复次数
        left, right = 0, max_possible + 1
        while left < right:
            mid = (left + right) // 2
            if check_repeating(mid):
                left = mid + 1
            else:
                right = mid
        
        return left - 1
    
    # 方法2：动态规划解法
    def maxRepeating2(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        if m > n:
            return 0
            
        # dp[i]表示以sequence[i]结尾的最大重复次数
        dp = [0] * n
        
        # 初始化：检查每个位置开始是否匹配一个word
        for i in range(n - m + 1):
            if sequence[i:i+m] == word:
                dp[i+m-1] = 1
        
        # 动态规划过程
        for i in range(m, n):
            if dp[i] == 1:  # 如果当前位置匹配一个word
                # 检查前面是否有连续匹配
                if i >= m and dp[i-m] > 0:
                    dp[i] = dp[i-m] + 1
        
        return max(dp)

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例
    test_cases = [
        ("ababc", "ab"),    # 2
        ("ababc", "ba"),    # 1
        ("ababc", "ac"),    # 0
        ("aaaa", "a"),      # 4
        ("abababab", "ab")  # 4
    ]
    
    print("方法1测试结果：")
    for sequence, word in test_cases:
        result = solution.maxRepeating(sequence, word)
        print(f"sequence: {sequence}, word: {word}, result: {result}")
    
    print("\n方法2测试结果：")
    for sequence, word in test_cases:
        result = solution.maxRepeating2(sequence, word)
        print(f"sequence: {sequence}, word: {word}, result: {result}")
