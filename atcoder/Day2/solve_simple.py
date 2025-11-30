def solve_recursive(s):
    total = 0
    
    def dfs(index, current_sum):
        nonlocal total
        print(index, s, total, current_sum)
        
        # 基底条件: 全ての文字を処理した
        if index == len(s):
            total += current_sum
            print(index, s, total, current_sum, 0)
            return
        
        # 選択肢1: ここで区切る(+を入れる)
        dfs(index + 1, current_sum + int(s[index]) )
        
        # 選択肢2: 次の文字と繋げる(+を入れない)
        dfs(index + 1, current_sum * 10 + int(s[index]) )
    
    # 最初の文字から開始
    dfs(1, int(s[0]))
    return total

print(solve_recursive("125"))