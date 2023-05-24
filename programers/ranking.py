# 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/49191
# 그래프 이론, 플로이드 워셜

INF = 9


def solution(n, results):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0

    for winner, loser in results:
        graph[winner][loser] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for row in graph:
        print(row)

    count = 0
    for i in range(1, n + 1):
        is_determined = True
        for j in range(1, n + 1):
            if graph[i][j] == INF and graph[j][i] == INF:
                is_determined = False
                break
        if is_determined:
            count += 1

    return count


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
