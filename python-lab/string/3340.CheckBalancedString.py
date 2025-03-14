# 3340. Check Balanced String

class Solution:
    def isBalanced(self, num: str) -> bool:
        # 计算奇数位和偶数位数字之和
        even_sum = 0
        odd_sum = 0
        
        for i, digit in enumerate(num):
            if i % 2 == 0:  # 偶数位（从0开始索引）
                even_sum += int(digit)
            else:  # 奇数位
                odd_sum += int(digit)
        
        # 检查是否平衡
        return even_sum == odd_sum
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.isBalanced("123"))
    print(solution.isBalanced("24123"))