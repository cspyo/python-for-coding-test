# Improved Dijkstra
# 최소힙 사용

import heapq
import sys

f=sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, d = map(int, f().rstrip().split())
    graph[a].append((b, d))

q=[]
heapq.heappush(q, (0,start))
distance[start]=0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for node, ndist in graph[now]:
        cost = dist+ndist
        if distance[node] > cost:
            distance[node] = cost
            heapq.heappush(q, (cost, node))

for i in range(1, n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])







