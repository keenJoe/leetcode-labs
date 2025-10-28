# 2379. Minimum Recolors to Get K Consecutive Black Blocks

'''
给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。

给你一个整数 k ，表示想要 连续 黑色块的数目。

每一次操作中，你可以选择一个白色块将它 涂成 黑色块。

请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。

 

示例 1：

输入：blocks = "WBBWWBBWBW", k = 7
输出：3
解释：
一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
得到 blocks = "BBBBBBBWBW" 。
可以证明无法用少于 3 次操作得到 7 个连续的黑块。
所以我们返回 3 。
示例 2：

输入：blocks = "WBWBBBW", k = 2
输出：0
解释：
不需要任何操作，因为已经有 2 个连续的黑块。
所以我们返回 0 。


使用滑动窗口实现
定长的滑动窗口
遍历每个字符
如果当前字符是 'W'，则操作次数加 1；
如果当前字符是 'B'，则操作次数不变；
当窗口右移到末尾时，返回操作次数。

但是这里存在一个重复的问题。
第一个窗口：WBBWWBB，操作 1 2 5 6 位置，操作 4 次；
第二个窗口：BBWWBBW，操作 1 2 5 6 位置，操作也是 4 次；
实际第一个和第二个窗口操作的字符一致，统计的数量也一致，但是需要重复统计。

为了避免重复计算，可以在滑动窗口时立刻更新操作次数。

'''

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = blocks[:k].count('W')
        min_operations = white_count

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white_count += 1
            
            if blocks[i - k] == 'W':
                white_count -= 1
            
            min_operations = min(min_operations, white_count)
        
        return min_operations
    
    # 这个更需要掌握，这个更有助于理解滑动窗口
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0, 0
        white_count = 0
        min_ops = float('inf')
        
        while right < len(blocks):
            # 扩展窗口：添加右边界
            if blocks[right] == 'W':
                white_count += 1
            right += 1
            
            # 收缩窗口：保持窗口大小为 k
            if right - left > k:
                if blocks[left] == 'W':
                    white_count -= 1
                left += 1
            
            # 当窗口大小等于 k 时，更新答案
            if right - left == k:
                min_ops = min(min_ops, white_count)
        
        return min_ops


if __name__ == "__main__":
    solution = Solution()
    blocks = "WBBWWBBWBW"
    k = 7
    print(solution.minimumRecolors(blocks, k))