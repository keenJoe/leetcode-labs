# 79. Word Search


'''
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
    输入: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    输出: true
    输入: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    输出: false

    回溯算法
    1. 遍历board，找到与word[0]相同的字母
    2. 以该字母为起点，向上下左右四个方向进行回溯
    3. 如果找到与word[1]相同的字母，继续回溯
    4. 如果找到与word[1]不同的字母，回溯到上一个字母
    5. 回溯到上一个字母后，再次从字符串的第一个字母开始回溯
'''

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def backtrack(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[k]:
                return False
            
            visited[i][j] = True
            res = backtrack(i + 1, j, k + 1) or backtrack(i - 1, j, k + 1) or backtrack(i, j + 1, k + 1) or backtrack(i, j - 1, k + 1)
            visited[i][j] = False
            return res
        
        # 从board的每一个位置开始回溯，如果找到与word[0]相同的字母，则继续回溯
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
    
if __name__ == "__main__":
    s = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(s.exist(board, word))

    word = "ABCB"
    print(s.exist(board, word))

    word = "SEE"
    print(s.exist(board, word))

