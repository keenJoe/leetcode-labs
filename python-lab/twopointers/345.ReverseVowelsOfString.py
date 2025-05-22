# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)  # 将字符串转换为列表
        left = 0
        right = len(s) - 1
        vowels = "aeiouAEIOU"  # 增加大写元音字母

        while left < right:
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            elif s_list[left] not in vowels:
                left += 1
            elif s_list[right] not in vowels:
                right -= 1
        
        return "".join(s_list)  # 将列表转换回字符串

if __name__ == "__main__":
    solution = Solution()
    s = "hello"
    print(solution.reverseVowels(s))
    print(solution.reverseVowels("leetcode"))  # 添加一个测试用例
