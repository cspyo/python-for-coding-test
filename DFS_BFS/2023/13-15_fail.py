# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

from collections import deque
# import sys
# sys.stdin.readline 으로 받아야함 입력이 너무 많음

INF = 1e9

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(n, x, graph):
    queue = deque()
    queue.append(x)

    distance = [INF for _ in range(n+1)]
    distance[x] = 0

    while queue:
        now = queue.popleft()
        for node in graph[now]:
            # 여기서도 모든 노드의 거리를 살펴봐버리니까 시간초과 나옴
            # distance[node]==INF인 애들만 그냥 바꿔주면 됨
            # min 안써도 됨
            distance[node] = min(distance[node], distance[now]+1)
            queue.append(node)

    return distance


def get_result(n, distance):
    if (distance.count(k) == 0):
        print(-1)
        return
    for i in range(n+1):
        if (distance[i] == k):
            print(i)


distance = bfs(n, x, graph)
get_result(n, distance)
