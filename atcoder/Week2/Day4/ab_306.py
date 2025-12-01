import functools

def solve():
    l = [5,4,1,3,2]

    l2 = sorted(l)
    print(l, l2) # l は変わっていない, l2 はソートされたリスト

    l3 = l.sort() # 記述しても l2 はリストにはなりません
    print(l3, l) # l はソートされる, l3 は None


def solve2():
    l = ["ba", "ac", "a", "abc"]
    l2 = [(1, 1), (0, 1), (1, 0)]
    l3 = [[1, 1], [0, 1], [1, 0]]
    l1 = sorted(l)
    l2 = sorted(l2)
    l3 = sorted(l3)
    print(l1)
    print(l2)
    print(l3)

def solve3():
    # 文字列 -> 各文字が辞書順でソートされ、1文字ずつのリストになる
    s = "atcoder"
    print(sorted(s))
    
    # タプル -> 要素がソートされ、リストになる
    a = (3, 1, 4, 1, 5)
    print(sorted(a))

def solve4():
    l = [1,2,3,4]
    l2 = sorted(l, reverse=True)
    print(l2) # [4, 3, 2, 1]

def solve5():
    l = [1,2,3,4]
    l.sort(reverse=True)
    print(l) # [4, 3, 2, 1]

# 「整数値のリストを、各値の下1桁でソートする」という問題
# 方法1: 評価値と元の要素からなるタプルのリストをソートする
def method1():
    l = [2, 6, 11, 100]
    l2 = [(v%10, v) for v in l] # (要素の下一桁, 要素) のリスト
    print(l2) # [(2, 2), (6, 6), (1, 11), (0, 100)]
    l2.sort()
    print(l2) # [(0, 100), (1, 11), (2, 2), (6, 6)]
    l = [item[1] for item in l2] # l2 の各要素から元の要素を抜き出す
    print(l) # [100, 11, 2, 6]

# 方法2: ソートの引数に評価値を与える関数を渡す
def method2():
    l = [2, 6, 11, 100]

    def func(x):
        return x % 10
    l.sort(key = func)
    print(l) # [100, 11, 2, 6]

    # これは次のように 1 行で記述することも可能:
    # l.sort(key = lambda x: x%10)
    
def method2_alpha():
    # x の降順にソート : reverse 引数を使わずに以下のように書くことも可能
    l = [2, 6, 11, 100]
    print(sorted(l, key = lambda x: -x)) # [100, 11, 6, 2]
    
    # タプルの2番目の要素でソート
    l = [(3,1), (4,2), (0,1)]
    print(sorted(l, key = lambda x: x[1])) # [(3, 1), (0, 1), (4, 2)]
    # 補足 : 「引き分け」の場合のソート順について
    # 上記の最後の例において、(3, 1) と (0, 1) は「タプルの2番目の要素」という評価基準では優劣が付きません。
    # このような場合は元のリストにおける並び順を保ったままになります。
    # 上記の例では (3, 1) が (0, 1) よりも先にある、という関係が保たれていることを確認できます。
    # ソートがこのような性質を持つ場合、安定であるといいます。

# 「タプル (a,b) と (c,d) に対して、 a * d < b * c ならば (a,b) が先になるようにする」という問題
def thema1():
    l = [(3,5), (1,3), (2,4)]
# 何らかの処理を行って [(1,3), (2,4), (3,5)] を得たい
    def cmp(x,y):
        # x,y : 長さ2のタプル -> 書きやすさのためアンパックしておく
        a,b = x
        c,d = y
        if a*d < b*c:
            return -2
        elif a*d == b*c:
            return 1
        else:
            return 4
    l.sort(key = functools.cmp_to_key(cmp)) # ↑で定義した cmp 関数を functools.cmp_to_key 関数に与える
    print(l) # [(1, 3), (2, 4), (3, 5)]

thema1()