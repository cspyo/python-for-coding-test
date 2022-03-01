# 전보

import heapq as hq
INF = int(1e9)
n,m,c = map(int, input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y,z=map(int, input().split())
    graph[x].append((y,z))


distance=[INF] * (n+1)

q=[]
hq.heappush(q, (0,c))
distance[c]=0
while q:
    cost, now = hq.heappop(q)
    for v, d in graph[now]:
        a=cost+d
        if distance[v]<a:
            continue
        distance[v]=a
        hq.heappush(q, (distance[v], v))

count=0
max_value=0
for i in distance:
    if i!=INF:
        count+=1
    max_value = max(max_value, i)

print(count-1, max_value)