# 2900. Longest Unequal Adjacent Groups Subsequence I

from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # 方法1：贪心算法
        def greedy_solution(words: List[str], groups: List[int]) -> List[str]:
            result = [words[0]]  # 初始化结果，包含第一个单词
            last_group = groups[0]  # 记录上一个选中元素的group值
            
            # 遍历剩余元素
            for i in range(1, len(words)):
                # 如果当前元素的group值与上一个不同，则选择它
                if groups[i] != last_group:
                    result.append(words[i])
                    last_group = groups[i]
            
            return result
        
        # 方法2：动态规划
        def dp_solution(words: List[str], groups: List[int]) -> List[str]:
            n = len(words)
            # dp[i]表示以i结尾的最长有效子序列长度
            dp = [1] * n
            # prev[i]记录最优解中i的前一个位置
            prev = [-1] * n
            
            # 记录全局最大长度和结束位置
            max_len = 1
            end_pos = 0
            
            for i in range(1, n):
                for j in range(i):
                    # 如果groups值不同且可以形成更长的序列
                    if groups[i] != groups[j] and dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
                        # 更新全局最优解
                        if dp[i] > max_len:
                            max_len = dp[i]
                            end_pos = i
            
            # 重建结果序列
            result = []
            while end_pos != -1:
                result.append(words[end_pos])
                end_pos = prev[end_pos]
            
            return result[::-1]  # 反转得到正确顺序
        
        # 使用贪心算法（更优解）
        return dp_solution(words, groups)

# 测试代码
def test_solution():
    solution = Solution()
    
    test_cases = [
        {
            "words": ["e","a","b"],
            "groups": [0,0,1],
            "expected": ["e","b"]
        },
        {
            "words": ["a","b","c","d"],
            "groups": [1,0,1,1],
            "expected": ["a","b","c"]
        },
        {
            "words": ["a","b","c"],
            "groups": [1,1,1],
            "expected": ["a"]
        }
    ]
    
    for i, test in enumerate(test_cases):
        result = solution.getLongestSubsequence(test["words"], test["groups"])
        print(f"测试用例 {i+1}:")
        print(f"输入: words = {test['words']}, groups = {test['groups']}")
        print(f"输出: {result}")
        print(f"期望: {test['expected']}")
        # print(f"结果: {'通过' if len(result) == len(test['expected'])} else '失败'}")
        print()

if __name__ == "__main__":
    test_solution()
