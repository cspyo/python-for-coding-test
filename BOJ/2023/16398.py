# 행성 연결
# https://www.acmicpc.net/problem/16398

import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
edges = []

for a in range(n):
    for b in range(a + 1, n):
        edges.append((graph[a][b], a, b))

edges.sort()


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
for edge in edges:
    cost, a, b = edge

    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)