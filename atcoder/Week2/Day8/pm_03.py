# 方法3.Itertools.product（最もシンプル）
from itertools import product
s = input()
digits = list(map(int, s))

for ops in product(['+', '-'], repeat=3):
    total =digits[0]
    exp = str(digits[0])
    
    for i, op in enumerate(ops):
        if op == '+':
            total += digits[i+1]
        else:
            total -= digits[i+1]
            
        exp += op + str(digits[i+1])
        
    if total == 7:
        print(exp+"=7")
        break