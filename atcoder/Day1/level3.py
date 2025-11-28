# 問題: 0と1だけで作れる2桁以下の数を全表示
def binary_numbers(current):
    if current > 99:
        return
    
    if current > 0:  # 0はスキップ
        print(current)
        binary_numbers(current * 10 + 0)  # 末尾に0追加
        
    binary_numbers(current * 10 + 1)  # 末尾に1追加

binary_numbers(0)
# 出力: 1, 10, 11