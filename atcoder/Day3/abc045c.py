import sys
input = sys.stdin.readline

def solve_abc045c(s):
    n = len(s)
    total = 0
    
    def dfs(index, current_value, sum_so_far):
        nonlocal total
                
        # 基底条件: 全ての文字を処理した
        if index == n:
            # 最後の数値を合計に加える
            final_sum = sum_so_far + current_value
            total += final_sum
            return
        
        # 選択肢1: ここで区切る(+を入れる)
        dfs(index + 1, 
            int(s[index]),
            sum_so_far + current_value)
        
        # 選択肢2: 次の文字と繋げる(+を入れない)
        dfs(index + 1, 
            current_value * 10 + int(s[index]),
            sum_so_far)
    
    # 最初の文字から開始
    dfs(1, int(s[0]), 0)
    return total

s = input().strip()
result = solve_abc045c(s)
print(result)