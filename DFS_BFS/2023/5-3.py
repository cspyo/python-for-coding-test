# 음료수 얼려먹기

import sys
f = sys.stdin.readline

example = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

n, m = map(int, f().rstrip().split())

graph = []
for i in range(n):
    graph.append((list(map(int, f().rstrip()))))

print(graph)


def dfs(x, y):
    if (x < 0 or y < 0 or x >= n or y >= m):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


count_ice_cream = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count_ice_cream += 1

print(count_ice_cream)
