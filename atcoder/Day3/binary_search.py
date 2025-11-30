# 遅い方法: O(N)
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # 右半分を探す
        else:
            right = mid - 1  # 左半分を探す
    
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(linear_search(arr, 1))  # 3
print(binary_search(arr, 7))  # 3