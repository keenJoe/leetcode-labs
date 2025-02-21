# 1299. Replace Elements with Greatest Element on Right Side

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 初始化最大值为-1（最右边元素的右侧最大值）
        curr_max = -1
        
        # 从右向左遍历
        for i in range(len(arr)-1, -1, -1):
            # 保存当前元素
            temp = arr[i]
            # 将当前位置替换为已知的最大值
            arr[i] = curr_max
            # 更新最大值（当前元素可能是下一个位置的右侧最大值）
            curr_max = max(curr_max, temp)
            
        return arr


if __name__ == "__main__":
    solution = Solution()
    print(solution.replaceElements([17, 18, 5, 4, 6, 1]))
