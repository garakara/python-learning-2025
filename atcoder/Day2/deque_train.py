from collections import deque

# dequeで実装(リストより高速)
queue = deque()

# 追加(enqueue)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

# 取り出し(dequeue)
print(queue.pop())  # 3 ← 最初に入れたものが出る
print(queue.popleft())  # 1
print(queue)  # deque([2])