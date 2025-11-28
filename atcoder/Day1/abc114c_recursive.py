def count_753(n):
    count = 0
    
    # 変数1:現在値, 変数2:3の存在確認, 変数3:5の存在確認,変数4:7の存在確認
    def dfs(current, has3, has5, has7):
        nonlocal count
        
        # 基底条件1: Nを超えたら終了
        if current > n:
            return
        
        # 基底条件2: 3,5,7全て含んでいたらカウント
        if has3 and has5 and has7:
            count += 1

        # 再帰呼び出し: 末尾に3,5,7を追加        
        dfs(current * 10 + 3, True, has5, has7)   # 3を追加
        dfs(current * 10 + 5, has3, True, has7)   # 5を追加
        dfs(current * 10 + 7, has3, has5, True)   # 7を追加

    # 0から開始(最初は何も含んでいない)
    dfs(0, False, False, False)
    return count

n = int(input())
print(count_753(n))