from itertools import product

arr = [1, 2, 3, 3, -4, 4, 1]
target = 10

# 各要素を選ぶ(1) or 選ばない(0)
for selection in product([0, 1], repeat=len(arr)):
    total = sum(arr[i] for i, s in enumerate(selection) if s == 1)
    print(total, selection)
    
    if total == target:
        selected = [arr[i] for i, s in enumerate(selection) if s == 1]
        print(f"できる! {selected}")
        break