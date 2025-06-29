# 冒泡排序

def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("排序后的数组：")
    print(sorted_arr)