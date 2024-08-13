import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx=[-1,0,0,1]
dy=[0,-1,1,0]

def bfs(time,x,y):
    visited=[[0 for _ in range(n)]for _ in range(n)]
    eat_lst=[]
    q=deque()
    q.append([time,x,y])
    visited[x][y]=1

    while q:
        time,x,y= q.popleft()
            
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if graph[nx][ny]==0 or graph[nx][ny]==size:
                    q.append([time+1,nx,ny])
                    visited[nx][ny]=1
                elif 0<graph[nx][ny]<size:
                    eat_lst.append([time+1,nx,ny])
                    visited[nx][ny]=1
                    
    if len(eat_lst)==0:
        return False
    else:
        return sorted(eat_lst)

for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            x=i
            y=j
size=2
eat=0
time=0

while True:
    graph[x][y]=0
    ans=bfs(0,x,y)
    if ans==False:
        print(time)
        break
    eat+=1
    if size==eat:
        size+=1
        eat=0

    x=ans[0][1]
    y=ans[0][2]
    time+=ans[0][0]