# 插入排序

def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        unsorted_value = arr[i]
        while i > 0 and arr[i - 1] > unsorted_value:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = unsorted_value
    return arr

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print(insert_sort(arr))