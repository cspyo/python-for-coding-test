# 연구소
# https://www.acmicpc.net/problem/14502


# 벽 3개를 세우는 경우의 수
# 벽 세우고 바이러스에서 bfs 나 dfs 돌리기
# 남은 안전 영역 수 구하기

import sys
import itertools
f = sys.stdin.readline

n, m = map(int, f().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, f().rstrip().split())))

# 벽을 놓을 수 있는 공간과 바이러스가 있는 곳 찾기
empty_place = []
viruses = []
for i in range(n):
    for j in range(m):
        if (graph[i][j] == 0):
            empty_place.append((i, j))
        elif (graph[i][j] == 2):
            viruses.append((i, j))


# 바이러스 확산
def spread(x, y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx < 0 or ny < 0 or nx >= n or ny >= m):
            continue
        if (graph[nx][ny] == 0):
            graph[nx][ny] = 2
            spread(nx, ny, graph)


# 벽 3개를 놓는 모든 방법 (순서 상관 없음)
make_walls = list(itertools.combinations(empty_place, 3))

safe_area = -1

# 벽은 놓는 모든 방법에 대해
for walls in make_walls:

    # 기존 지도 깊은 복사
    tmp_graph = [item[:] for item in graph]

    # 벽 놓기
    for wall in walls:
        tmp_graph[wall[0]][wall[1]] = 1

    # 바이러스 확산
    for virus in viruses:
        spread(virus[0], virus[1], tmp_graph)

    # 안전 영역 계산
    sum = 0
    for row in tmp_graph:
        sum += row.count(0)

    # 기존 안전 영역보다 더 넓은지 확인
    safe_area = max(sum, safe_area)

print(safe_area)
