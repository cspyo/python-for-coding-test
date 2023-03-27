# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

from collections import deque
import sys

f = sys.stdin.readline
INF = 1e9

n, m, k, x = map(int, f().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

queue = deque()
queue.append(x)

distance = [-1] * (n+1)
distance[x] = 0

while queue:
    now = queue.popleft()
    for next in graph[now]:
        if (distance[next] == -1):
            distance[next] = distance[now]+1
            queue.append(next)

check = False
for i in range(n+1):
    if (distance[i] == k):
        print(i)
        check = True
if not check:
    print(-1)
