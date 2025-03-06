# 357. Count Numbers with Unique Digits

'''
    给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。
    如果 n = 1，则所有可能的数字为 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，共有 10 个。
    如果 n = 2，则应该排除11, 22, 33, 44, 55, 66, 77, 88, 99，则有9 * 9 = 81个，再加上10个0-9，共91个。
    如果 n = 3，
        100～199中，排除101 110 111 112 113 114 115 116 117 118 119；121 122 133 144 155 166 177 188 199；
    
    分析思路
    这道题可以通过组合计数的方法来解决。我们可以按照数字的位数来分类讨论：
    1位数（0-9）
    所有1位数都满足条件
    共有10个数字：0,1,2,3,4,5,6,7,8,9
    
    2位数（10-99）
    首位可以是1-9（9种选择）
    第二位可以是0-9中除了首位已用的数字（9种选择）
    共有9×9=81个数字
    
    3位数（100-999）
    首位可以是1-9（9种选择）
    第二位可以是0-9中除了首位已用的数字（9种选择）
    第三位可以是0-9中除了前两位已用的数字（8种选择）
    共有9×9×8=648个数字
    
    4位数（1000-9999）
    首位：9种选择
    第二位：9种选择
    第三位：8种选择
    第四位：7种选择
    共有9×9×8×7=4,536个数字
    
    依此类推...
    通项公式
    对于k位数（k≥2）：
    数量 = 9 × 9 × 8 × ... × (11-k)
    即：9 × P(9,k-1)，其中P表示排列数
    总数 = 所有不同位数的数量之和
    
'''

class Solution:
    def countNumbersWithUniqueDigits_1(self, n: int) -> int:
        # 处理特殊情况
        if n == 0:
            return 1  # 只有0
        
        # 初始化结果为1位数的情况
        result = 10
        # 当前乘积
        current = 9
        # 可用数字数量
        available = 9
        
        # 从2位数开始计算到n位数
        for i in range(2, min(n + 1, 11)):  # 最多只能到10位数
            # 计算当前位可以使用的数字种类
            current *= available
            # 累加到结果中
            result += current
            # 可用数字减少一个
            available -= 1
        
        return result
    
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        # 使用回溯法计算
        self.count = 1  # 初始值为1，表示只有0的情况
        self.backtrack(n, 0, set())
        return self.count
    
    def backtrack(self, n, current_len, used_digits):
        # 已经达到长度上限，不再继续
        if current_len == n:
            return
        
        # 选择当前位可以使用的数字
        for digit in range(10):
            # 如果是首位，不能选0
            if current_len == 0 and digit == 0 and n > 1:
                continue
            
            # 如果数字已经使用过，跳过
            if digit in used_digits:
                continue
            
            # 选择这个数字
            used_digits.add(digit)
            # 计数加1
            self.count += 1
            # 继续构建下一位
            self.backtrack(n, current_len + 1, used_digits)
            # 回溯，移除这个数字
            used_digits.remove(digit)

if __name__ == "__main__":
    solution = Solution()
    print(solution.countNumbersWithUniqueDigits(2))
