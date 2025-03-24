# 2255. Count Prefixes of a Given String

from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(1 for word in words if s.startswith(word))
    
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.countPrefixes(["a", "b", "c", "ab", "bc", "abc"], "abc"))
