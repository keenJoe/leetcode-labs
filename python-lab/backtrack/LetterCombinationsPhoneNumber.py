# 17. Letter Combinations of a Phone Number

'''
    1、维护一个数字和字母的映射关系；
        映射关系是字典和数组：
            digit_to_char = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]
            }
    2、遍历数字，选择一个字母加入路径中；
    3、递归，开始选择下个数字，然后选择一个字母加入路径中；
    4、回溯，移除最后一个字母；
    5、重复2-4，直到所有数字都用过一次；
    6、返回结果。
'''

from typing import List


class Solution:    
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_char = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]
            }
        result = []
        length = len(digits)

        def backtrack(path):
            # 如果路径长度等于数字长度，则将路径加入结果中
            if len(path) == length:
                str = ''
                for char in path:
                    str += char
                if str:
                    result.append(str)
                return
            
            # 遍历数字，返回对应的字母列表
            chars = digit_to_char[digits[len(path)]]
            # 遍历字母列表，选择一个字母加入路径中
            for char in chars:
                path.append(char)
                backtrack(path)
                path.pop()
                
        backtrack([])
        return result
    
    '''
        1、维护一个数字和字母的映射关系；
        2、遍历数字，选择一个字母加入路径中；
        3、递归，开始选择下个数字，然后选择一个字母加入路径中；
        4、回溯，移除最后一个字母；
        5、重复2-4，直到所有数字都用过一次；
        6、返回结果。
    '''
    
    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_char = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        result = []
        length = len(digits)
    
        def backtrack(index, current_str):
            # 使用字符串而不是列表来构建结果，避免后续的连接操作
            if len(current_str) == length:
                result.append(current_str)
                return
            
            # 直接在字符串上操作，避免append和pop操作
            for char in digit_to_char[digits[index]]:
                backtrack(index + 1, current_str + char)
    
        backtrack(0, "")
        return result
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))
