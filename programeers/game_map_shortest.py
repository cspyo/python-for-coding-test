# 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

# 이 문제는 DFS로 풀면 효율성에서 다 틀린다.

from collections import deque

INF = int(1e9)


def bfs(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = deque([])
    q.append((0, 0, 1))
    maps[0][0] = 0
    answer = INF
    while q:
        x, y, d = q.popleft()
        if x == n-1 and y == m-1:
            answer = min(answer, d)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append((nx, ny, d+1))
    return answer


def solution(maps):
    answer = bfs(maps)
    if answer >= INF:
        return -1
    else:
        return answer
