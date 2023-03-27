# 경쟁적 전염
# https://www.acmicpc.net/problem/18405

from collections import deque
import sys
f = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, f().rstrip().split())))

s, x, y = map(int, input().split())
# 문제는 (1,1) 부터 시작 / 실제 2차원 배열은 (0,0) 시작
x = x-1
y = y-1

# 바이러스 위치 탐색 및 저장, 정렬
# 모든 초마다 큐를 만듬. 근데 1만초까지니까 큐가 1만개 생김...너무 많아.
viruses = [deque() for _ in range(s+1)]
list = []
for i in range(n):
    for j in range(n):
        if (graph[i][j] != 0):
            list.append((graph[i][j], i, j))
# viruses 를 정렬한 다음 큐로 변환
list.sort(key=lambda x: x[0])
viruses[0] = deque(list)

# 바이러스 확산


def spread(virus, s):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        x = dx[i] + virus[1]
        y = dy[i] + virus[2]
        if (x < 0 or y < 0 or x >= n or y >= n):
            continue
        if (graph[x][y] == 0):
            graph[x][y] = virus[0]
            viruses[s].append((graph[x][y], x, y))


for i in range(1, s+1):
    while (viruses[i-1]):
        virus = viruses[i-1].popleft()
        spread(virus, i)

print(graph[x][y])
