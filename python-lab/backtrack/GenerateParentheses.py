# 22. Generate Parentheses

from typing import List

'''
    1、问题1：是不是需要遍历的长度  = 2 * n，还是生成两个数组，然后遍历两个数组
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(left: int, right: int, path: str):
            if len(path) == 2 * n:
                result.append(path)
                return
            
            if left < n:
                backtrack(left + 1, right, path + '(')
            
            if right < left:
                backtrack(left, right + 1, path + ')')
                
        backtrack(0, 0, '')
        return result
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(left: int, right: int, current: List[str]):
            if len(current) == 2 * n:
                result.append(''.join(current))
                return
            
            if left < n:
                current.append('(')  # 添加左括号
                backtrack(left + 1, right, current)
                current.pop()  # 需要pop，因为修改了current
            
            if right < left:
                current.append(')')  # 添加右括号
                backtrack(left, right + 1, current)
                current.pop()  # 需要pop，因为修改了current
    
        backtrack(0, 0, [])
        return result
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))