# 다익스트라 최소힙 버전 구현하기

import sys
import heapq as hq
f = sys.stdin.readline

INF = int(1e9)
n, m = map(int, f().split())
start = int(input())
# 노드 연결 정보 저장 2차원리스트
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

# 연결 정보 입력
for _ in range(m):
    node_now, node_goal, d = map(int, f().split())
    graph[node_now].append((node_goal, d))


def dijkstra(start):
    q = []
    distance[start] = 0
    hq.heappush(q, (distance[start], start))
    while (q):
        d, now = hq.heappop(q)
        if (visited[now]):
            continue
        visited[now] = True
        for next_node, node_distance in graph[now]:
            cost = d + node_distance
            if (distance[next_node] > cost):
                distance[next_node] = cost
                hq.heappush(q, (cost, next_node))


dijkstra(start)

for i in range(1, n+1):
    if (distance[i] == INF):
        print("Can't go")
    else:
        print(distance[i])
