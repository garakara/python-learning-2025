arr = [1, 2, 3, 3, -4, 4, 1]
target = 10

def subset_sum(index, current_sum, selected):
    if current_sum == target:
        print(f"できる! {selected}")
        return True
    
    if index >= len(arr) or current_sum > target:
        return False
    
    # 選ぶ
    if subset_sum(index+1, current_sum+arr[index], selected+[arr[index]]):
        return True
    
    # 選ばない
    if subset_sum(index+1, current_sum, selected):
        return True
    
    return False

subset_sum(0, 0, [])