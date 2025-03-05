# 306. Additive Number

from typing import List

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        def valid(start: int, length: int) -> bool:
            """检查从start开始，长度为length的子串是否是有效数字"""
            # 如果长度大于1，且以0开头，则无效
            if length > 1 and num[start] == '0':
                return False
            return True
        
        def backtrack(index: int, prev1: int, prev2: int, count: int) -> bool:
            # 如果已经处理到字符串末尾，且至少有3个数字，则找到解
            if index == n:
                return count >= 3
            
            # 尝试不同长度的数字
            curr = 0
            for i in range(index, n):
                curr = curr * 10 + int(num[i])
                # 检查数字是否有效（不能有前导零）
                if not valid(index, i - index + 1):
                    break
                    
                # 如果已经有两个以上的数字，检查是否满足累加条件
                if count >= 2:
                    if curr < prev1 + prev2:
                        continue
                    if curr > prev1 + prev2:
                        break
                
                # 当前数字满足条件，继续递归
                if backtrack(i + 1, prev2, curr, count + 1):
                    return True
            
            return False
        
        # 从头开始尝试不同的前两个数字
        return backtrack(0, 0, 0, 0)

    # 添加辅助方法用于打印和验证结果
    def print_sequence(self, num: str) -> None:
        """打印累加序列"""
        def find_sequence(num: str) -> List[int]:
            n = len(num)
            for i in range(1, n-1):
                if i > 1 and num[0] == '0':
                    break
                for j in range(i+1, n):
                    if j-i > 1 and num[i] == '0':
                        break
                    num1 = int(num[:i])
                    num2 = int(num[i:j])
                    sequence = [num1, num2]
                    
                    start = j
                    while start < n:
                        next_num = num1 + num2
                        next_str = str(next_num)
                        if not num.startswith(next_str, start):
                            break
                        sequence.append(next_num)
                        start += len(next_str)
                        num1, num2 = num2, next_num
                        
                    if start == n:
                        return sequence
            return []
            
        sequence = find_sequence(num)
        if sequence:
            print(f"'{num}' 是累加数:")
            print(" + ".join(map(str, sequence[:-1])))
            print(f"= {sequence[-1]}")
        else:
            print(f"'{num}' 不是累加数")

if __name__ == "__main__":
    s = Solution()
    print(s.isAdditiveNumber("112358"))
    print(s.isAdditiveNumber("199100199"))