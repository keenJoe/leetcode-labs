# 1561. Maximum Number of Coins You Can Get

from typing import List

class Solution:
    # 太妙了，了解了切片的用法
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[len(piles)//3::2])