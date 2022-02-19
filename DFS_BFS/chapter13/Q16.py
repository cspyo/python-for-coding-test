# 연구소
# BOJ 14502

# 1세개를 두는 모든 경우의 수 + 모든 2에서의 dfs
# 일단 아이디어는 맞았는데 벽3개를 두는 모든 경우의 수를 구현하지 못했음
# combinations 라이브러리 사용해서 구현 완료~
from itertools import combinations
import sys
f = sys.stdin.readline

n, m = map(int, f().split())
jido = []

for i in range(n):
    jido.append(list(map(int, f().split())))


tmp_jido = [item[:] for item in jido]
can_make_wall = []
for i in range(n):
    for j in range(m):
        if jido[i][j]==0:
            can_make_wall.append((i,j))


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


result=0
for x in combinations(can_make_wall, 3):
    # 벽 세우기
    x=list(x)
    for a in x:
        tmp_jido[a[0]][a[1]]=1
    # 바이러스 퍼트리기
    for i in range(n):
        for j in range(m):
            if tmp_jido[i][j]==2:
                virus(i,j)
    # 안전영역 검사
    result=max(result,get_safe_area())
    # 벽 원상복구
    tmp_jido = [item[:] for item in jido]

print(result)

