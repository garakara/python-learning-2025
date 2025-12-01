import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import bisect
import math
input = sys.stdin.readline

# キーポイント
# 関数定義: def 関数名(パラメータ):
# 戻り値を返すには, return文を用いる
# 関数外の変数を更新するには, global文を用いる

# ex1. 単純な関数
def print_numbers(n, m):
    for i in range(n, m):
        print(f"カウントアップ{i+1}")

# ex2. 戻地を持つ関数定義
def add_one(a):
    return a + 1

# ex3. 関数定義のテクニック
def my_min(a, b):
    if a < b:
        return a
    else:
        return b
    
# ex4.return文の特性
def add_one_2(a):
    return a + 1
    print("ここに到達しない")
    return a + 2
    print("もちろんここに到達しない")

# ex5. if文の工夫
def my_min_2(a, b):
    if a < b:
        return a   
    return b

# ex6. 関数の処理を早期に終了する目的でreturn文を用いる
# returnが実行されるため、そこで関数の処理が終了する。
def print_a_is_7(a):
    if a == 7:
        print("a is 7")
        return
    print("a is not 7")

# ex7. 関数内の変数(グローバル関数に値を代入したい場合)
def update_a(val):
    global a
    a = val

# ex8. listを変更するケースは、global文は必要ない
li = []
def update_li_1(val):
    li.append(val)

# ex9. listにglobal文が必要になるときの記述（値を代入するケース）
li = []
def update_li_2(val):
    global li
    li = li + [val]

# ex10. nonlocal
def get_1():
    value = 0
    def set_1():
        nonlocal value
        # ここで用いている value はグローバル変数ではないので、global は使えない
        value = 1 # Error: local variable 'value' referenced before assignment
    set_1()
    return value

if __name__ == '__main__':
    
    # 入力文字方式
    # n = int(input())
    # n, m = map(int, input().split())

    # ex1で使用
    # print_numbers(n, m)

    # ex2で使用
    # print(add_one(n))

    # ex3で使用
    # print(my_min(n, m))

    # ex4で使用
    # print(add_one_2(n))

    # ex5で使用
    # print(my_min_2(n, m))
    
    # ex6で使用
    # print_a_is_7(n)
    
    # ex7で使用
    # a = 0
    # update_a(1)
    # print(a)
    # a = 5
    # print(a)
    
    # ex8で使用
    # for i in [8, 5, 3]:
    #     update_li_1(i)
    # print(li) # [1] と出力される

    # ex9で使用
    # for i in [8, 5, 3]:
    #     update_li_2(i)
    # print(li) # [1] と出力される
    
    # ex10で使用
    print(get_1())
