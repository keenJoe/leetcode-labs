# 401. Binary Watch

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def backtrack(start: int, hours: int, mins: int, count: int):
            # 当已经选择了足够的LED时，检查时间是否有效
            if count == turnedOn:
                if hours <= 11 and mins <= 59:
                    # 格式化时间字符串
                    time = f"{hours}:{mins:02d}"
                    result.append(time)
                return
            
            # 从start开始遍历所有LED
            for i in range(start, 10):
                if i < 4:  # 前4个LED代表小时
                    # 点亮这个小时LED
                    new_hours = hours | (1 << i)
                    if new_hours <= 11:  # 确保小时有效
                        backtrack(i + 1, new_hours, mins, count + 1)
                else:  # 后6个LED代表分钟
                    # 点亮这个分钟LED
                    new_mins = mins | (1 << (i - 4))
                    if new_mins <= 59:  # 确保分钟有效
                        backtrack(i + 1, hours, new_mins, count + 1)
        
        result = []
        backtrack(0, 0, 0, 0)
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.readBinaryWatch(1))
