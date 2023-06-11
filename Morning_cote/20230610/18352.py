# 특정 거리 도시 찾기
# https://www.acmicpc.net/problem/18352

import sys
import heapq as hq

input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    distance[start] = 0
    hq.heappush(q, (distance[start], start))
    while q:
        d, now = hq.heappop(q)
        if distance[now] < d:
            continue
        
        for next_node in graph[now]:
            cost = d + 1
            if cost<distance[next_node]:
                distance[next_node] = cost
                hq.heappush(q, (cost, next_node))

def for_answer():
    flag = True
    for i in range(1, n+1):
        if distance[i] == k:
            flag = False
            print(i)
    if flag:
        print(-1)

dijkstra(x)
for_answer()
    
