# 미래 도시
# 내가 푼 해답
# 다익스트라랑 BFS 혼합해서 두번 돌림
# 1-->k + k-->x
from collections import deque

INF=int(1e9)

n, m = map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
x, k =  map(int, input().split())

# 그냥 BFS 두번 돌리면 되는건가?

def dijkstra(start, end):
    d=[INF]*(n+1)
    d[start]=0
    q=deque([start])
    while q:
        a = q.popleft()
        dist=d[a]+1
        for v in graph[a]:
            if d[v]<dist:
                continue
            d[v]=dist
            q.append(v)
    return d[end]

result = dijkstra(1, k) + dijkstra(k, x)

if result>=INF:
    print(-1)
else:
    print(result)
