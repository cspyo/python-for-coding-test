# 퍼즐 조각 채우기
# https://school.programmers.co.kr/learn/courses/30/lessons/84021
# DFS/BFS

from collections import deque


def rotate(graph):
    new_graph = zip(*graph[::-1])
    return [list(item) for item in new_graph]


def bfs(x, y, graph, n, num):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # bfs로 탐색하면서 찾은 블록을 (0,0) 기준으로 저장하기
    q = deque([])
    q.append([x, y, 0, 0])
    # 방문처리
    graph[x][y] = 2
    block = [(0, 0)]

    while q:
        px, py, base_x, base_y = q.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 게임 보드랑 테이블의 visited 플래그가 달라서 이런 식으로 처리
                if graph[nx][ny] == num or graph[nx][ny] == 2:
                    continue
                else:
                    position_x = base_x + dx[i]
                    position_y = base_y + dy[i]
                    q.append([nx, ny, position_x, position_y])
                    graph[nx][ny] = 2
                    block.append((position_x, position_y))
    return block


def solution(game_board, table):
    answer = 0
    # 게임보드에 비어 있는 공간 확인하기
    blanks = []
    n = len(game_board)
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                blanks.append(bfs(i, j, game_board, n, 1))

    # 회전 4번
    for k in range(4):
        table = rotate(table)
        table_tmp = [item[:] for item in table]
        for i in range(n):
            for j in range(n):
                # 어차피 블록을 하나씩 확인한다.
                if table_tmp[i][j] == 1:
                    block = bfs(i, j, table_tmp, n, 0)
                    # 만약 블록과 맞는 빈칸이 있으면
                    # 빈칸 목록에서 블록을 지우고, answer에 그 길이만큼 더하기
                    # 테이블에 있는 블록도 썼다는 것을 나타내기 위해
                    # 해당 블록의 visited가 끝내진 지금 현 상태의 테이블을 저장한다
                    if block in blanks:
                        answer += len(block)
                        blanks.remove(block)
                        table = [item[:] for item in table_tmp]
                    # 해당 블록에 맞는 빈칸이 없으면 블록을 안 쓴거니까
                    # visited 를 풀어주기 위해 기존 table로 교체
                    else:
                        table_tmp = [item[:] for item in table]

    return answer
