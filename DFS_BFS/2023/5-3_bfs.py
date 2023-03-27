from collections import deque
import sys

f = sys.stdin.readline


n, m = map(int, f().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, f().rstrip())))


def bfs(x, y):
    if (graph[x][y] == 1):
        return False
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while (queue):
        a, b = queue.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            if (graph[nx][ny] == 1):
                continue
            graph[nx][ny] = 1
            queue.append((nx, ny))
    return True


count_ice_cream = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j):
            count_ice_cream += 1

print(count_ice_cream)
