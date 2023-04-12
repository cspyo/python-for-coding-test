# 전보
# dijkstra

import heapq

n, m, c = map(int, input().split())


graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def solution(n, m, c, graph):
    # 도시 개수, 총 걸리는 시간
    answer = [0, 0]
    INF = int(1e9)
    shortest = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, c))
    shortest[c] = 0

    while q:
        dist, now = heapq.heappop(q)
        if shortest[now] < dist:
            continue
        for node, distance in graph[now]:
            cost = dist + distance
            if (cost < shortest[node]):
                shortest[node] = cost
                heapq.heappush(q, (cost, node))

    count_city = 0
    max_distance = 0
    for i in range(1, n+1):
        if shortest[i] == INF or i == c:
            continue
        else:
            count_city += 1
            max_distance = max(max_distance, shortest[i])

    return (count_city, max_distance)


print(solution(n, m, c, graph))
