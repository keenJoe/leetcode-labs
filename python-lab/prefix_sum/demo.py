def suffix_sum_basic():
    # 原始数组
    nums = [10,4,-8,7]
    n = len(nums)
    
    # 构建后缀和数组
    # suffix[i] 表示从 nums[i] 到 nums[n-1] 的和
    suffix = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        suffix[i] = suffix[i + 1] + nums[i]

    # 构建前缀和数组
    # prefix[i] 表示 nums[0] 到 nums[i] 的和
    prefix = [0] * (n + 1)  # 多一个位置，方便计算
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    
    # 查询示例：计算区间 [left, right] 的和
    def query_range(left: int, right: int) -> int:
        return suffix[left] - suffix[right + 1]
    
    # 使用示例
    print(f"原始数组: {nums}")
    print(f"后缀和数组: {suffix}")


     # 查询示例：计算区间 [left, right] 的和
    def query_range(left: int, right: int) -> int:
        return prefix[right + 1] - prefix[left]
    
    # 使用示例
    print(f"原始数组: {nums}")
    print(f"前缀和数组: {prefix}")


suffix_sum_basic()