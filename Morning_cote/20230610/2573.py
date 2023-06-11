# 빙산
# https://www.acmicpc.net/problem/2573

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y, graph_tmp):
    if graph_tmp[x][y] <= 0:
        return False
    
    dx = [1, -1 , 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque([])
    q.append((x, y))
    graph_tmp[x][y] = -1 # 방문처리
    
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            
            if graph_tmp[nx][ny] <= 0:
                continue
            else:
                q.append((nx, ny))
                graph_tmp[nx][ny] = -1
    
    return True

def check_zero(x, y, graph_tmp):
    dx = [1, -1 , 0, 0]
    dy = [0, 0, 1, -1]
    
    count=0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if graph_tmp[nx][ny] == 0:
            count+=1
    return count

def a_year_ago():
    graph_tmp = [item[:] for item in graph]
    for i in range(1, n-1):
        for j in range(1, m-1):
            graph[i][j]-=check_zero(i,j, graph_tmp)
            if graph[i][j]<0:
                graph[i][j] = 0
    
def check_ice():
    graph_tmp = [item[:] for item in graph]
    check = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if bfs(i, j, graph_tmp):
                check+=1
    return check

def for_answer():
    count=0
    while(True):
        a_year_ago()
        count+=1
        check = check_ice()
        if check>1:
            return count
        if check==0:
            return 0
        
print(for_answer())
