stack = []

# 追加(push)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

# 取り出し(pop)
print(stack.pop())  # 3 ← 最後に入れたものが出る
print(stack)
print(stack.pop())  # 2
print(stack)
print(stack.pop())  # [1]
print(stack)

# 空かチェック
if stack:
    print("still remain")
else:
    print("not yet")