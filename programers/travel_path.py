# 여행 경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164#
# DFS
result = []


def dfs(cnt, now, n, graph, path):
    global result

    # 티켓을 다 소진하면 마지막 공항을 더하고 경로 리스트에 추가
    if cnt == n:
        path += now
        result.append(path)
    else:
        # path를 배열로 append를 하면 재귀가 될 때마다 이전 path에도 영향을 미침
        # 따라서 문자열로 현재까지의 경로를 저장
        path += now+','
        # 공항 경로 백트래킹
        for i in range(len(graph[now])):
            airport, used = graph[now][i]
            if not used:
                graph[now][i][1] = True
                dfs(cnt+1, airport, n, graph, path)
                graph[now][i][1] = False


def solution(tickets):
    global result

    # 중복 제거를 위한 set으로 공항 추출
    airports = set([])
    for a, b in tickets:
        airports.add(a)
        airports.add(b)

    # 딕셔너리 자료구조 활용
    # {'ICN': [['JFK', False], ['IAD', False]]} 이 형식으로 공항간 연결을 저장
    graph = {}
    for airport in airports:
        graph[airport] = []
    for a, b in tickets:
        graph[a].append([b, False])

    # 시작은 ICN에서 DFS 돌리기
    now = "ICN"
    dfs(1, now, len(tickets)+1, graph, "")

    # 알파벳 순으로 앞서는 경로를 추출
    result.sort()
    answer = list(result[0].split(','))

    return answer
