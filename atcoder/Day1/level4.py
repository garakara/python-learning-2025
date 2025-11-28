def count_35(current, n):
    if current > n:
        return 0
    
    # 現在の数を1としてカウント + 再帰の結果
    count = 1
    print(current, count, n, "check1")
    
    count += count_35(current * 10 + 3, n)
    print(current, count, n, "check2")

    count += count_35(current * 10 + 5, n)    
    print(current, count, n, "check3")
    return count

# 3から開始、5から開始を合計
result = count_35(3, 100) + count_35(5, 100)
print(result)