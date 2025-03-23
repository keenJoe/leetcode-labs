# 2116. Check if a Parentheses String Can Be Valid

"""
    1、使用栈来记录需要修改的括号位置
    2、如果是左括号，则入栈
    3、如果是右括号，则出栈
    4、如果栈不为空，则需要修改；
    5、判断栈的元素数量，再确定locked中能修改的元素数量是否满足条件
    6、满足条件
        1、locked中位置为0的元素，且是左括号
"""

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # 如果s的长度为奇数，则直接返回False
        if len(s) % 2 == 1:
            return False

        left_stack = []    # 存储未匹配的左括号位置
        right_stack = []   # 存储未匹配的右括号位置
        unlocked = []      # 存储可变位置

        # 第一次遍历：处理固定括号的匹配，同时记录可变位置
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                left_stack.append(i)
            elif s[i] == ')':
                if left_stack:  # 有左括号可以匹配
                    left_stack.pop()
                else:  # 没有左括号可以匹配
                    right_stack.append(i)

        # 如果完全匹配，直接返回True
        if not left_stack and not right_stack:
            return True

        # 检查是否有足够的可变位置来平衡未匹配的括号
        unmatched = len(left_stack) + len(right_stack)
        if len(unlocked) < unmatched:
            return False

        # 检查从左到右是否可以平衡
        count = 0
        for i in range(len(s)):
            if locked[i] == '1':
                count += 1 if s[i] == '(' else -1
            else:
                count += 1  # 可变位置先假设为左括号
            if count < 0:  # 如果任何位置右括号过多
                return False

        # 检查从右到左是否可以平衡
        count = 0
        for i in range(len(s)-1, -1, -1):
            if locked[i] == '1':
                count += 1 if s[i] == ')' else -1
            else:
                count += 1  # 可变位置先假设为右括号
            if count < 0:  # 如果任何位置左括号过多
                return False

        return True

    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:  # 长度为奇数时直接返回False
            return False
            
        def check(s: str, locked: str, open_char: str) -> bool:
            balance = 0  # 平衡值
            wild = 0    # 可改变的括号数量
            
            # 根据遍历方向决定范围
            start = 0 if open_char == '(' else len(s) - 1
            end = len(s) if open_char == '(' else -1
            step = 1 if open_char == '(' else -1
            
            for i in range(start, end, step):
                if locked[i] == '1':
                    # 固定的括号
                    balance += 1 if s[i] == open_char else -1
                else:
                    # 可改变的括号
                    wild += 1
                
                # 检查是否违反规则
                if wild + balance < 0:
                    return False
            
            # 检查最终状态
            return balance <= wild and (wild - balance) % 2 == 0
        
        # 需要同时满足从左到右和从右到左的检查
        return check(s, locked, '(') and check(s, locked, ')')

if __name__ == "__main__":
    solution = Solution()
    s = "()))"
    locked = "0101"
    print(solution.canBeValid(s, locked))