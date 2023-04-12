# 미래 도시
# 플로이드 워셜

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    # 간선이 존재하면 양방향 이기에 양쪽으로 1 설정
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())


def solution(graph, x, k):

    # 플로이드 알고리즘
    for i in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

    # 시작 지점인 1에서 k를 거치고 k에서 x로 가는 거리
    result = graph[1][k] + graph[k][x]
    if result >= INF:
        return -1
    else:
        return result


print(solution(graph, x, k))
