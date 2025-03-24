# 338. Counting Bits

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # i & (i-1) 可以消除最右边的1，通过这种方式可以利用之前的结果
            dp[i] = dp[i & (i-1)] + 1
            
        return dp