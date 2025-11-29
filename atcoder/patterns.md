# 再帰パターン集

## パターン1: 全探索(2択)
```python
def dfs(index, current):
    if index == n:
        # 終了条件
        return
    dfs(index+1, current+選択肢A)
    dfs(index+1, current+選択肢B)
```
使用例: ABC079C, ABC045C

## パターン2: 再帰生成
```python
def dfs(current):
    if current > limit:
        return
    # カウント処理
    dfs(current * 10 + A)
    dfs(current * 10 + B)
```
使用例: ABC114C