arr = [2, 1, 3, -7, 11]
target = 10

for bits in range(2**len(arr)):
    total = 0
    selected = []
    
    for i in range(len(arr)):
        if bits & (1 << i):
            total += arr[i]
            selected.append(arr[i])
            
    if total == target:
        print(f"できる！ {selected}")
        break