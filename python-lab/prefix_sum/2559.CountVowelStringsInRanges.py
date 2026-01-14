# 2559. Count Vowel Strings in Ranges

'''
给你一个下标从 0 开始的字符串数组 words 以及一个二维整数数组 queries 。

每个查询 queries[i] = [li, ri] 会要求我们统计在 words 中下标在 li 到 ri 范围内（包含 这两个值）
并且以元音开头和结尾的字符串的数目。

返回一个整数数组，其中数组的第 i 个元素对应第 i 个查询的答案。

注意：元音字母是 'a'、'e'、'i'、'o' 和 'u' 。

 

示例 1：
输入：words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
输出：[2,3,0]
解释：以元音开头和结尾的字符串是 "aba"、"ece"、"aa" 和 "e" 。
查询 [0,2] 结果为 2（字符串 "aba" 和 "ece"）。
查询 [1,4] 结果为 3（字符串 "ece"、"aa"、"e"）。
查询 [1,1] 结果为 0 。
返回结果 [2,3,0] 。

示例 2：
输入：words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
输出：[3,2,1]
解释：每个字符串都满足这一条件，所以返回 [3,2,1] 。


这次的前缀和需要转换，需要判断每个单词是不是以元音开头和结尾。

'''

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0] * (len(words) + 1)
        # 构建前缀和
        for i in range(len(words)):
            # 判断单词的开头和结尾是否都是元音
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]

        # 使用前缀和
        result = []
        for query in queries:
            left, right = query
            result.append(prefix[right + 1] - prefix[left])
        
        return result

if __name__ == "__main__":
    solution = Solution()
    words = ["aba", "bcb", "ece", "aa", "e"]
    queries = [[0, 2], [1, 4], [1, 1]]
    print(solution.vowelStrings(words, queries))
    