# 3306. Count of Substrings Containing Every Vowel and K Consonants II

# class Solution:
#     def countOfSubstrings(self, word: str, k: int) -> int:
#         """
#         计算包含所有元音字母且恰好有k个辅音字母的子串数量
        
#         Args:
#             word: 输入字符串
#             k: 目标辅音字母数量
            
#         Returns:
#             满足条件的子串数量
#         """
#         vowels = {'a', 'e', 'i', 'o', 'u'}
#         n = len(word)
#         result = 0
        
#         # 预处理：标记每个字符是元音还是辅音
#         is_vowel = [c in vowels for c in word]
        
#         # 特殊情况：k=0，只需要找包含所有元音且没有辅音的子串
#         if k == 0:
#             for left in range(n):
#                 vowel_set = set()
#                 for right in range(left, n):
#                     if not is_vowel[right]:  # 遇到辅音直接终止
#                         break
#                     vowel_set.add(word[right])
#                     if len(vowel_set) == 5:  # 找到包含所有元音的子串
#                         result += 1
#             return result
        
#         # 一般情况：使用滑动窗口
#         for left in range(n):
#             # 初始化元音计数和辅音计数
#             vowel_count = {v: 0 for v in vowels}
#             consonant_count = 0
            
#             # 优化：如果剩余长度不足以包含所有元音和k个辅音，直接跳过
#             if n - left < 5 + k:
#                 continue
                
#             for right in range(left, n):
#                 if is_vowel[right]:
#                     vowel_count[word[right]] += 1
#                 else:
#                     consonant_count += 1
                
#                 # 如果辅音超过k，不再扩展
#                 if consonant_count > k:
#                     break
                
#                 # 检查是否满足条件：恰好k个辅音且包含所有元音
#                 if consonant_count == k and all(vowel_count[v] > 0 for v in vowels):
#                     result += 1
        
#         return result
    
#     def countOfSubstrings_optimized(self, word: str, k: int) -> int:
#         """
#         高度优化版本，适用于超大规模输入
#         """
#         vowels = {'a', 'e', 'i', 'o', 'u'}
#         n = len(word)
        
#         # 预处理：标记每个字符是元音还是辅音
#         is_vowel = [c in vowels for c in word]
        
#         # 特殊情况：k=0
#         if k == 0:
#             return self._count_zero_consonants(word, is_vowel)
        
#         # 使用位掩码优化元音检查
#         vowel_masks = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
#         ALL_VOWELS = 31  # 11111 in binary
        
#         result = 0
        
#         for left in range(n):
#             # 优化：如果剩余长度不足，直接跳过
#             if n - left < 5 + k:
#                 continue
                
#             vowel_mask = 0
#             consonant_count = 0
            
#             for right in range(left, n):
#                 if is_vowel[right]:
#                     vowel_mask |= vowel_masks[word[right]]
#                 else:
#                     consonant_count += 1
                
#                 if consonant_count > k:
#                     break
                
#                 # 使用位掩码检查是否包含所有元音
#                 if consonant_count == k and vowel_mask == ALL_VOWELS:
#                     result += 1
        
#         return result
    
#     def _count_zero_consonants(self, word, is_vowel):
#         """处理k=0的特殊情况"""
#         vowels = {'a', 'e', 'i', 'o', 'u'}
#         n = len(word)
#         result = 0
        
#         for left in range(n):
#             vowel_set = set()
#             for right in range(left, n):
#                 if not is_vowel[right]:
#                     break
#                 vowel_set.add(word[right])
#                 if len(vowel_set) == 5:
#                     result += 1
        
#         return result
    

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        def count(m: int) -> int:
            n, res, consonants = len(word), 0, 0
            occur = {}
            j = 0
            for i in range(n):
                while j < n and (consonants < m or len(occur) < 5):
                    if word[j] in vowels:
                        occur[word[j]] = occur.get(word[j], 0) + 1
                    else:
                        consonants += 1
                    j += 1
                if consonants >= m and len(occur) == 5:
                    res += n - j + 1
                if word[i] in vowels:
                    occur[word[i]] -= 1
                    if occur[word[i]] == 0:
                        del occur[word[i]]
                else:
                    consonants -= 1
            return res
        return count(k) - count(k + 1)


if __name__ == "__main__":
    solution = Solution()
    
    # 基本测试用例
    test_cases = [
        ("aeioqq", 1, 1),
        ("aeiou", 0, 1),
        ("ieaouqqieaouqq", 1, 3)
    ]
    
    for i, (word, k, expected) in enumerate(test_cases):
        result = solution.countOfSubstrings(word, k)
        print(f"Test case {i+1}: {result} {'✓' if result == expected else '✗'}")
    
    # 验证优化版本
    for i, (word, k, expected) in enumerate(test_cases):
        result = solution.countOfSubstrings_optimized(word, k)
        print(f"Optimized test {i+1}: {result} {'✓' if result == expected else '✗'}")
    
    # 性能测试
    import time
    
    # 生成大规模测试用例
    large_test = "aeiou" * 200 + "q" * 200
    
    print("\n性能测试:")
    
    start = time.time()
    result1 = solution.countOfSubstrings(large_test, 100)
    time1 = time.time() - start
    
    start = time.time()
    result2 = solution.countOfSubstrings_optimized(large_test, 100)
    time2 = time.time() - start
    
    print(f"基础版本: {result1} (用时 {time1:.4f}s)")
    print(f"优化版本: {result2} (用时 {time2:.4f}s)")
    print(f"性能提升: {time1/time2:.2f}x")