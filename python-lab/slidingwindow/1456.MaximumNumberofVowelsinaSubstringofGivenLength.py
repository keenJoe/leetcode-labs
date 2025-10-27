# 1456. Maximum Number of Vowels in a Substring of Given Length

'''
示例 1：
输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。

示例 2：
输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。

示例 3：
输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。

示例 4：
输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。

示例 5：
输入：s = "tryhard", k = 4
输出：1

使用滑动窗口
固定窗口的长度是 3
开始遍历每个字符
判断当前字符是否是元音字母。
    如果是，则元音字母数量加 1，并将当前元音字母数量与最大元音字母数量比较，更新最大元音字母数量。然后右移窗口，继续判断下一个字符。
    如果不是，则继续右移窗口，继续判断下一个字符。
    当窗口右移到末尾时，返回最大元音字母数量。
但是子串是不连续的，是不是要先保持左指针不变，然后当有指针到达末尾时，再移动左指针
    子串是连续的，子序列是非连续的
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        current_vowels = 0  # 当前窗口的元音数量
        max_vowels = 0       # 历史最大元音数量
        left = 0
        right = 0
        
        while right < len(s):
            # 1. 加入右边界字符
            if s[right] in vowels:
                current_vowels += 1  # ← 修改点1
            
            right += 1
            
            # 2. 当窗口大小超过 k 时，移除左边界字符
            while right - left > k:  # ← 修改点2：改为 > k，不是 > k
                if s[left] in vowels:
                    current_vowels -= 1  # ← 修改点3
                left += 1
            
            # 3. 当窗口大小等于 k 时，更新最大值
            if right - left == k:  # ← 修改点4
                max_vowels = max(max_vowels, current_vowels)  # ← 修改点5
        
        return max_vowels

    
    def maxVowelsUsingSet(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}  # ← 优化1：使用 set
        
        # 阶段1：初始化前 k 个字符的窗口
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        
        max_vowels = current_vowels  # 初始最大值
        
        # 阶段2：滑动窗口（从第 k+1 个字符开始）
        for i in range(k, len(s)):
            # 同时处理：加入新字符 s[i]，移除旧字符 s[i-k]
            if s[i] in vowels:
                current_vowels += 1
            if s[i - k] in vowels:  # ← 优化2：直接用索引，不需要 left 指针
                current_vowels -= 1
            
            max_vowels = max(max_vowels, current_vowels)  # ← 优化3：只在需要时更新
        
        return max_vowels

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxVowels("abciiidef", 3))