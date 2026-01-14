# 前缀和（Prefix Sum）详解

## 一、背景：从一道经典题目说起

### LeetCode 303. 区域和检索 - 数组不可变

**题目描述**：给定一个整数数组 `nums`，实现一个类来处理多次区间求和查询。

```python
numArray = NumArray([-2, 0, 3, -5, 2, -1])
numArray.sumRange(0, 2)  # return 1 = (-2) + 0 + 3
numArray.sumRange(2, 5)  # return -1 = 3 + (-5) + 2 + (-1)
numArray.sumRange(0, 5)  # return -3
```

### 朴素解法

```python
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])  # 每次查询 O(n)
```

**问题**：每次查询都需要遍历区间，时间复杂度 O(k)，k 为区间长度。当查询次数 m 很大时，总时间复杂度为 O(m × k)。

---

## 二、前缀和的核心思想

### 2.1 本质：预计算 + 空间换时间

前缀和的核心优化思想是：**减少重复计算**

- 在初始化时，一次性预计算所有前缀和
- 查询时，通过 O(1) 的减法运算得到区间和

### 2.2 关键转化

> **把「区间求和」转化为「两点相减」**

```
sum(nums[left:right+1]) = prefix[right+1] - prefix[left]
```

---

## 三、前缀和的两种定义

### 3.1 不包含自己（推荐）

```python
# prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
# 即：prefix[i] 表示前 i 个元素的和，不包含第 i 个元素
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]
```

**特点**：
- 数组长度为 n + 1
- `prefix[0] = 0`，天然处理边界
- 区间和公式：`sum[left, right] = prefix[right + 1] - prefix[left]`

**图示**：
```
nums:      [-2,   0,   3,  -5,   2,  -1]
索引:        0    1    2    3    4    5

prefix:   [0,  -2,  -2,   1,  -4,  -2,  -3]
索引:       0    1    2    3    4    5    6
           ↑
        prefix[0]=0 是边界哨兵
```

### 3.2 包含自己

```python
# prefix[i] = nums[0] + nums[1] + ... + nums[i]
# 即：prefix[i] 表示从 0 到 i 的元素之和，包含第 i 个元素
prefix = [0] * n
prefix[0] = nums[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + nums[i]
```

**特点**：
- 数组长度为 n
- 需要特判 `left = 0` 的情况
- 区间和公式：
  - `left > 0` 时：`sum[left, right] = prefix[right] - prefix[left-1]`
  - `left = 0` 时：`sum[0, right] = prefix[right]`（需特判！）

---

## 四、如何选择前缀和定义？

### 4.1 解题两步法

1. **明确统计区间**：题目要求的是什么区间？
   - 左闭右闭 [left, right]（最常见）
   - 左闭右开 [left, right)
   - 其他

2. **选择前缀和定义**：根据区间选择合适的定义

### 4.2 选择建议

| 区间类型 | 推荐定义 | 公式 |
|---------|---------|------|
| [left, right] 闭区间 | 不包含自己 | `prefix[right+1] - prefix[left]` |
| [left, right) 左闭右开 | 不包含自己 | `prefix[right] - prefix[left]` |

**实战口诀**：推荐默认使用「不包含自己」的前缀和，因为：
- ✅ 与 Python 切片语义一致
- ✅ `prefix[0] = 0` 天然处理边界
- ✅ 公式统一，无需特判

### 4.3 本题分析

LeetCode 303 要求 `sumRange(left, right)` 返回 `nums[left] + ... + nums[right]`，即**闭区间 [left, right]**。

使用「不包含自己」的前缀和：
- `prefix[right + 1]` = nums[0] + ... + nums[right]（包含 right）
- `prefix[left]` = nums[0] + ... + nums[left-1]（不包含 left）
- 相减刚好得到 [left, right] 闭区间的和

---

## 五、时间复杂度对比

| 操作 | 朴素解法 | 前缀和优化 |
|------|----------|-----------|
| 初始化 | O(1) | O(n) |
| 每次查询 | O(k)，k为区间长度 | **O(1)** |
| m次查询总计 | O(m × k) | **O(n + m)** |

当查询次数 m 很大时，优化效果非常明显！

---

## 六、前缀和模板

### 6.1 标准模板（推荐）

```python
class PrefixSum:
    """前缀和模板 - 不包含自己的定义"""
    
    def __init__(self, nums: List[int]):
        """
        构建前缀和数组
        prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
        """
        n = len(nums)
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
    
    def query(self, left: int, right: int) -> int:
        """
        查询闭区间 [left, right] 的和
        时间复杂度：O(1)
        """
        return self.prefix[right + 1] - self.prefix[left]
```

### 6.2 一行构建（Python 技巧）

```python
from itertools import accumulate

# 使用 accumulate 构建前缀和，initial=0 表示 prefix[0]=0
prefix = list(accumulate(nums, initial=0))

# 查询 [left, right] 区间和
def query(left, right):
    return prefix[right + 1] - prefix[left]
```

### 6.3 LeetCode 303 完整解答

```python
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # 构建前缀和数组，prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
        # prefix[0] = 0，这样处理边界更方便
        n = len(nums)
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # 区间和 = prefix[right+1] - prefix[left]
        return self.prefix[right + 1] - self.prefix[left]
```

---

## 七、总结

### 前缀和的核心要点

1. **思想**：预计算 + 空间换时间，把区间求和转化为两点相减
2. **定义选择**：优先使用「不包含自己」的定义，避免边界特判
3. **解题步骤**：
   - 明确题目要求的区间类型
   - 选择合适的前缀和定义
   - 推导区间和公式

### 适用场景

- 多次区间求和查询
- 子数组和相关问题
- 二维矩阵区域和（扩展为二维前缀和）

### 记忆口诀

> **prefix[0] = 0 是哨兵，区间求和两点减**
> **右边加一左边原，闭区间和立刻算**
