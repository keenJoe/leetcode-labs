# 212. Word Search II

from typing import List


class Solution:
    def findWords_1(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        result = []
        def backtrack(i, j, k, word):
            if k == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[k]:
                return False
            
            visited[i][j] = True
            res = backtrack(i + 1, j, k + 1, word) or backtrack(i - 1, j, k + 1, word) or backtrack(i, j + 1, k + 1, word) or backtrack(i, j - 1, k + 1, word)
            visited[i][j] = False
            return res
        
        # 从board的每一个位置开始回溯，如果找到与word[0]相同的字母，则继续回溯
        for word in words:
            for i in range(m):
                for j in range(n):
                    if backtrack(i, j, 0, word):
                        result.append(word) 
        return result
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []
            
        # 构建字典树
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word  # 使用'#'标记单词结尾，并存储完整单词
        
        def dfs(i: int, j: int, node: dict) -> None:
            # 如果找到单词（'#'标记存在）
            if '#' in node:
                result.add(node['#'])
            
            # 保存当前字母，以便回溯时恢复
            char = board[i][j]
            board[i][j] = '.'  # 标记已访问
            
            # 四个方向搜索
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if (0 <= ni < m and 0 <= nj < n and 
                    board[ni][nj] != '.' and 
                    board[ni][nj] in node):
                    dfs(ni, nj, node[board[ni][nj]])
            
            # 恢复当前字母
            board[i][j] = char
        
        result = set()
        m, n = len(board), len(board[0])
        
        # 从每个位置开始搜索
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]])
        
        return list(result)
    
if __name__ == "__main__":
    s = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    print(s.findWords(board, words))

    board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
    words = ["oa","oaa"]
    print(s.findWords(board, words))
