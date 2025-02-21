# 624. Maximum Distance in Arrays

from typing import List

'''
    1、使用第一个数组的最大和最小值初始化；
        如果第一个数组的长度为1，那么最大值和最小值相同；
    2、遍历后续的数组，更新最大和最小值；
    3、计算最大距离；
'''


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # min_val = arrays[0][0]
        # max_val = arrays[0][-1]

        # a = abs(arrays[1][0] - max_val)
        # b = abs(arrays[1][-1] - min_val)
        # if a > b:
        #     min_val = arrays[1][0]
        # else:
        #     max_val = arrays[1][-1]

        # for i in range(2, len(arrays)):
        #     if arrays[i][0] < min_val and arrays[i][-1] > max_val:
        #         a = abs(arrays[i][0] - min_val)
        #         b = abs(arrays[i][-1] - max_val)
        #         if a > b:
        #             min_val = arrays[i][0]
        #         else:
        #             max_val = arrays[i][-1]
        #     elif arrays[i][0] < min_val:
        #         min_val = arrays[i][0]
        #     elif arrays[i][-1] > max_val:
        #         max_val = arrays[i][-1]

        # print(min_val, max_val)
        # return abs(max_val - min_val)
        # 初始化结果和第一个数组的最大最小值
        result = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        # 从第二个数组开始遍历
        for i in range(1, len(arrays)):
            # 计算当前数组与之前数组的最大距离
            result = max(result,
                        abs(arrays[i][-1] - min_val),  # 当前数组最大值与之前最小值的差
                        abs(arrays[i][0] - max_val))    # 当前数组最小值与之前最大值的差
            
            # 更新全局最大最小值
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
    
        return result


if __name__ == "__main__":
    arrays = [[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
    print(Solution().maxDistance(arrays))
