from collections import deque

def solution(maps):
    answer = 0
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    n = len(maps)
    m = len(maps[0])
    
    def bfs():
        queue = deque()
        queue.append((0, 0))
        while queue:
            cur_y, cur_x = queue.popleft()
            
            for i in range(4):
                nx, ny = cur_x + dx[i], cur_y + dy[i]
                
                if 0 <= nx < m and 0 <= ny < n:
                    if maps[ny][nx] == 0:
                        continue
                        
                    if maps[ny][nx] == 1:
                        maps[ny][nx] = maps[cur_y][cur_x] + 1
                        queue.append((ny, nx))
    bfs()
    
    
    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]