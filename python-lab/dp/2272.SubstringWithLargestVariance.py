# 2272. Substring With Largest Variance

class Solution:
    def largestVariance(self, s: str) -> int:
        def kadane(ch1: str, ch2: str) -> int:
            # 统计剩余字符数量
            remaining_ch2 = sum(1 for c in s if c == ch2)
            result = 0
            cnt1 = cnt2 = 0
            
            for c in s:
                if c != ch1 and c != ch2:
                    continue
                    
                if c == ch1:
                    cnt1 += 1
                else:  # c == ch2
                    cnt2 += 1
                    remaining_ch2 -= 1
                
                # 只有当有ch2时才更新结果
                if cnt2 > 0:
                    result = max(result, cnt1 - cnt2)
                
                # 如果当前子串的ch1比ch2少，且后面还有ch2，则重新开始计数
                if cnt1 < cnt2 and remaining_ch2 > 0:
                    cnt1 = cnt2 = 0
            
            return result

        # 获取字符串中所有不同的字符
        chars = set(s)
        max_variance = 0
        
        # 尝试所有可能的字符对
        for ch1 in chars:
            for ch2 in chars:
                if ch1 != ch2:
                    # 正向和反向各计算一次，取最大值
                    forward = kadane(ch1, ch2)
                    backward = kadane(ch2, ch1)
                    max_variance = max(max_variance, forward, backward)
        
        return max_variance

if __name__ == "__main__":
    solution = Solution()
    # 测试用例
    print(solution.largestVariance("aababbb"))  # 应该输出 3
    print(solution.largestVariance("abcde"))    # 应该输出 0
    print(solution.largestVariance("lripaa")) # 应该输出 1

