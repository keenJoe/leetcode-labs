# 22. Generate Parentheses

from typing import List

'''
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。
    1、终止条件：如果当前路径的长度等于2 * n，则将当前路径加入到结果中（当然，需要判断当前路径是否有效）
    2、回溯条件：
        1、如果左括号小于n，则可以添加左括号
        2、如果右括号小于左括号，则可以添加右括号
        
    没有使用for循环，因为选择的范围是确定的，就是左括号和右括号，所以不需要for循环
    其次，其他需要for循环因为需要遍历，但是这里不需要，因为左括号和右括号是确定的
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(left, right, path):
            if len(path) == 2 * n:
                res.append(path)
                return 
            
            if left < n:
                backtrack(left + 1, right, path + '(')
            if right < left:
                backtrack(left, right + 1, path + ')')
                

        backtrack(0, 0, '')
        return res
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))