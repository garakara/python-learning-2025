# 方法2.ビット全探索（シンプル）
# メリット：再帰不要、上から下に読める, デメリット：ビット演算が必要
s = input()
digits = list(map(int, s))

for bits in range(8):
    total = digits[0]
    exp = str(digits[0])
    
    for i in range(3):
        if bits & (1 << i):
            total += digits[i+1]
            exp += "+" + str(digits[i+1])
            
        else:
            total -= digits[i+1]
            exp += "-" + str(digits[i+1])
            
    if total == 7:
        print(exp + "=7")
        break