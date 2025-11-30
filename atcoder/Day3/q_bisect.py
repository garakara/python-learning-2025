import bisect

arr = [1, 3, 5, 7, 9]  # ソート済み配列

# 1. bisect_left: 値を挿入する位置(左端)
pos = bisect.bisect_left(arr, 5)
print(pos)  # 2 (インデックス2の位置に5がある)

# 2. bisect_right: 値を挿入する位置(右端)
pos = bisect.bisect_right(arr, 5)
print(pos)  # 3 (5の右側)

# 3. 「x以上の要素数」を数える
pos = len(arr) - bisect.bisect_left(arr, 5)
print(pos)

# 4. 「xより小さい要素数」を数える
pos = bisect.bisect_left(arr, 6)
print(pos)

# 5. 「xより大きい要素数」を数える
pos = len(arr) - bisect.bisect_right(arr, 8)
print(pos)