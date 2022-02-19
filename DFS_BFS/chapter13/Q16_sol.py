# 연구소

import sys
f = sys.stdin.readline

n, m = map(int, f().split())
jido = []

for i in range(n):
    jido.append(list(map(int, f().split())))


tmp_jido = [[0]*m for _ in range(n)]

result=0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if tmp_jido[nx][ny]==0:
            tmp_jido[nx][ny]=2
            virus(nx,ny)

def get_safe_area():
    result=0
    for i in range(n):
        for j in range(m):
            if tmp_jido[i][j]==0:
                result+=1
    return result


def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                tmp_jido[i][j]=jido[i][j]
        for i in range(n):
            for j in range(m):
                if tmp_jido[i][j]==2:
                    virus(i,j)
        result=max(result,get_safe_area())
        return
    # 벽 3개를 세우는 것도 이런 방식으로 dfs 사용해서 할 수 있음
    # 생각하기가 쉽지 않음..
    for i in range(n):
            for j in range(m):
                if jido[i][j]==0:
                    jido[i][j]=1
                    count+=1
                    dfs(count)
                    jido[i][j]=0
                    count-=1

dfs(0)
print(result)

