from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        # 辅助函数：判断是否是回文
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        # 核心回溯函数
        def backtrack(s: str, start: int, path: List[str]):
            if start == len(s):  # 终止条件：处理完所有字符
                res.append(path[:])
                return
            for i in range(start, len(s)):  # 尝试所有可能的分割点
                if is_palindrome(s[start:i+1]):  # 剪枝：只有当前子串是回文才继续
                    path.append(s[start:i+1])     # 做出选择
                    backtrack(s, i+1, path)       # 递归处理剩余部分
                    path.pop()                    # 撤销选择（回溯）
        
        backtrack(s, 0, [])
        return res 