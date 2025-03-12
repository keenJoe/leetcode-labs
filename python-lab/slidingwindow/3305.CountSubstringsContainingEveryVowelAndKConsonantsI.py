# 3305. Count of Substrings Containing Every Vowel and K Consonants I

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        n = len(word)
        
        # 对每个可能的左边界
        for left in range(n):
            vowel_count = {v: 0 for v in vowels}
            consonant_count = 0
            
            # 向右扩展窗口
            for right in range(left, n):
                if word[right] in vowels:
                    vowel_count[word[right]] += 1
                else:
                    consonant_count += 1
                
                # 如果辅音超过k，不再扩展
                if consonant_count > k:
                    break
                
                # 检查是否满足条件
                if consonant_count == k and all(vowel_count[v] > 0 for v in vowels):
                    count += 1
        
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.countOfSubstrings("abcabc", 3))
    print(solution.countOfSubstrings("abcabc", 2))
    print(solution.countOfSubstrings("abcabc", 1))