# 경쟁적 전염
# BOJ 18405

from collections import deque
import sys
f=sys.stdin.readline

n, k = map(int, f().split())

data=[]
virus_data=[]
for i in range(n):
    data.append(list(map(int, f().split())))
    for j in range(n):
        if data[i][j]!=0:
            virus_data.append([data[i][j],i,j])

s, x, y = map(int, f().split())

 
virus_data.sort(key=lambda x : x[0])
virus_queue = deque(virus_data)
count=len(virus_data)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def virus(v, x, y):
    global count
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        if data[nx][ny]==0:
            data[nx][ny]=v
            virus_queue.append([v,nx,ny])
            count+=1

for _ in range(s):
    # 1초에 바이러스 갯수가 한사이클만 돌게 해야하기에 count가 필요
    for _ in range(count):
        a = virus_queue.popleft()
        count-=1
        virus(a[0],a[1],a[2])

print(data[x-1][y-1])

