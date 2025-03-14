# 17. Letter Combinations of a Phone Number

"""
    1、使用回溯法
    2、构建数字和字母的对应表
    3、遍历字符串，从0开始，遍历到digits的最后一个字符
    4、在回溯函数中，如果当前遍历到的字符串长度等于digits的长度，则将当前的组合加入到结果中
    5、否则，遍历当前数字对应的字母，将字母加入到当前的组合中，然后递归调用回溯函数
    6、回溯函数结束后，将当前的字母从组合中移除
    7、返回结果
"""

from typing import List


class Solution:    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dic = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }
        res = []
        def backtrack(index, path):
            if len(path) == len(digits):
                res.append(path)
                return
            
            for letter in dic[digits[index]]:
                backtrack(index + 1, path + letter)
                # 回溯，但是在这里不需要移除，因为path是字符串，是不可变对象
        
        backtrack(0, '')
        return res
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))
