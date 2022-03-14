# 특정 거리의 도시 찾기
# BOJ 18352

from collections import deque
import sys
f=sys.stdin.readline

n, m, k, x = map(int, f().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    i, a = map(int, f().split())
    graph[i].append(a)

d=[-1]*(n+1)

queue = deque([x])
d[x]=0
while queue:
    now = queue.popleft()
    for next in graph[now]:
        if d[next]==-1:
            d[next]=d[now]+1
            queue.append(next)
    
check=False
for i in range(1,n+1):
    if d[i]==k:
        print(i)
        check=True
if not check:
    print(-1)



