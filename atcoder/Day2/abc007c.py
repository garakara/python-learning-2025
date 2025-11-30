from collections import deque

def solve_bfs():
    H, W = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    sy -= 1; sx -= 1; gy -= 1; gx -= 1  # 0-indexed
    
    maze = [input() for _ in range(H)]
    
    # BFS初期化
    queue = deque([(sy, sx, 0)])  # (y, x, distance)
    visited = [[False] * W for _ in range(H)]
    visited[sy][sx] = True
    
    # 4方向
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        y, x, dist = queue.popleft()
        
        # ゴール到達
        if y == gy and x == gx:
            print(dist)
            return
        
        # 4方向を探索
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            # 範囲外チェック
            if not (0 <= ny < H and 0 <= nx < W):
                continue
            
            # 壁チェック
            if maze[ny][nx] == '#':
                continue
            
            # 訪問済みチェック
            if visited[ny][nx]:
                continue
            
            visited[ny][nx] = True
            queue.append((ny, nx, dist + 1))

solve_bfs()