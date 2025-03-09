# 2269. Find the K-Beauty of a Number

'''
    1、遍历num，从左到右，每次取k个数字，计算其美丽值；
    2、如果美丽值是k的倍数，则计数器加1；
    3、返回计数器。
'''

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        count = 0
        for i in range(len(num_str) - k + 1):
            # 取k个数字，确保长度为k
            sub_num = int(num_str[i:i+k])
            # 确保sub_num不为0，且num能被sub_num整除
            if sub_num != 0 and num % sub_num == 0:
                count += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.divisorSubstrings(240, 2))
