# 1963. Minimum Number of Swaps to Make the String Balanced

"""
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        # 记录未匹配的右括号数量
        unmatched = 0
        # 记录最大未匹配数量
        max_unmatched = 0
        
        # 遍历字符串
        for char in s:
            if char == '[':
                # 遇到左括号，如果有未匹配的右括号，就匹配掉一个
                # 还有一种可能，先遇到[
                unmatched -= 1
            else:  # char == ']'
                # 遇到右括号，未匹配数量加1
                unmatched += 1
                # 更新最大未匹配数量
                max_unmatched = max(max_unmatched, unmatched)
        
        # 需要的最小交换次数
        return (max_unmatched + 1) // 2

if __name__ == "__main__":
    s = Solution()
    print(s.minSwaps("][]["))      # 输出：1
    print(s.minSwaps("]]][[["))    # 输出：2
    print(s.minSwaps("[]"))        # 输出：0