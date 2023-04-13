# 합승 택시 요금
# https://school.programmers.co.kr/learn/courses/30/lessons/72413

def solution(n, s, a, b, fares):
    INF = int(1e9)

    # 모든 노드에서 모든 노드로 가는 비용 저장할 테이블 생성
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

    # 나 자신으로 가는 비용은 0
    for i in range(1, n+1):
        graph[i][i] = 0

    # 양방향이므로 양쪽에 가는 비용 초기화
    for fare in fares:
        i, j, cost = fare
        graph[i][j] = cost
        graph[j][i] = cost

    # 플로이드로 각 노드에서 노드로 가는 최단거리 계산
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    # s에서 i로 가고 i에서 a,b로 각각 가는 비용을 계산하고
    # 가장 작은 값을 저장
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, graph[s][i]+graph[i][a]+graph[i][b])

    return answer
