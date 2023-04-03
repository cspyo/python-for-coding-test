# 개선된 다익스트라

import heapq as hq
import sys

f = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    now, goal, distance = map(int, f().split())
    graph[now].append((goal, distance))

INF = int(1e9)
distance_table = [INF]*(n+1)
visited = [False]*(n+1)


def dijkstra(start):
    q = []
    distance_table[start] = 0
    hq.heappush(q, (distance_table[start], start))

    while q:
        distance, node = hq.heappop(q)
        # if (visited[node]):
        #     continue
        # visited[start] = True
        if (distance_table[node] < distance):
            continue
        for next_node, node_distance in graph[node]:
            cost = distance+node_distance
            if (distance_table[next_node] > cost):
                distance_table[next_node] = cost
                hq.heappush(q, (cost, next_node))


dijkstra(start)

for i in range(1, n+1):
    if (distance_table[i] == INF):
        print("Can't go")
    else:
        print(distance_table[i])


# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
