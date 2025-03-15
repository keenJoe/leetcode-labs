# 3110. Score of a String

class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        计算字符串的分数，定义为相邻字符ASCII码差值绝对值的和
        
        Args:
            s: 输入字符串
            
        Returns:
            字符串的分数
        """
        if not s or len(s) < 2:
            return 0
            
        total_score = 0
        
        # 遍历字符串，计算相邻字符的ASCII码差值绝对值
        for i in range(1, len(s)):
            # 计算当前字符与前一个字符的ASCII码差值绝对值
            diff = abs(ord(s[i]) - ord(s[i-1]))
            total_score += diff
        
        return total_score
    
    # 优化版本：使用zip函数简化代码
    def scoreOfString_optimized(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0
            
        # 使用zip将相邻字符配对，然后计算差值绝对值的和
        return sum(abs(ord(curr) - ord(prev)) for prev, curr in zip(s, s[1:]))


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例
    test_cases = [
        "abcd",       # |a-b| + |b-c| + |c-d| = 1 + 1 + 1 = 3
        "acac",       # |a-c| + |c-a| + |a-c| = 2 + 2 + 2 = 6
        "leetcode",   # |l-e| + |e-e| + |e-t| + |t-c| + |c-o| + |o-d| + |d-e| = 7 + 0 + 15 + 14 + 12 + 11 + 1 = 60
        "z",          # 单个字符，返回0
        "",           # 空字符串，返回0
        "aA",         # |a-A| = 32
        "123",        # |1-2| + |2-3| = 1 + 1 = 2
        "abcba"       # |a-b| + |b-c| + |c-b| + |b-a| = 1 + 1 + 1 + 1 = 4
    ]
    
    for tc in test_cases:
        score = solution.scoreOfString(tc)
        optimized_score = solution.scoreOfString_optimized(tc)
        
        print(f"字符串 '{tc}' 的分数: {score}")
        assert score == optimized_score, f"结果不一致: {score} vs {optimized_score}"
        
        # 详细计算过程
        if tc and len(tc) >= 2:
            print("计算过程:")
            for i in range(1, len(tc)):
                diff = abs(ord(tc[i]) - ord(tc[i-1]))
                print(f"|{tc[i-1]}-{tc[i]}| = |{ord(tc[i-1])}-{ord(tc[i])}| = {diff}")
        print()
