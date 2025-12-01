# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
A = [1, 7, 15]
B = [2, 9, 7]
answer = False

# ex1: 多重ループ break文の工夫
for a in A:
    for b in B:
        print(a, b)
        if a == b:
            answer = True
            print("ループを完全に抜けた")
            break
    if answer == True:
        break
if answer:
    print("YES")
else:
    print("NO")
    
# ex2: 多重ループの部分を関数化し、returnを用いて抜ける方法
def func():
    for i in range(3):
        for j in range(3):
            print(i, j)
            if i == 2 and  j == 1:
                print("iとjの値が指定値なので終了。")
                return
            
func()