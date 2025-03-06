# 473. Matchsticks to Square

'''
    1、将数组分成4个相等的部分
    2、计算和，如果和不能被4整除，则返回False
    3、使用回溯法，尝试将数组分成4个相等的部分
'''

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        edge_length = total_length // 4
        matchsticks.sort(reverse=True)
        self.edge_length = edge_length
        self.matchsticks = matchsticks
        return self.backtrack(0, 0, 0, 0, 0)
    
    def backtrack(self, edge1, edge2, edge3, edge4, index):
        if index == len(self.matchsticks):
            return edge1 == edge2 == edge3 == edge4 == self.edge_length
        
        if edge1 > self.edge_length or edge2 > self.edge_length or edge3 > self.edge_length or edge4 > self.edge_length:
            return False
        
        curr = self.matchsticks[index]
        
        if self.backtrack(edge1 + curr, edge2, edge3, edge4, index + 1):
            return True
        if self.backtrack(edge1, edge2 + curr, edge3, edge4, index + 1):
            return True
        if self.backtrack(edge1, edge2, edge3 + curr, edge4, index + 1):
            return True
        if self.backtrack(edge1, edge2, edge3, edge4 + curr, index + 1):
            return True
        
        return False
            
            
if __name__ == "__main__":
    solution = Solution()
    print(solution.makesquare([1,1,2,2,2]))
    print(solution.makesquare([3,3,3,3,4]))