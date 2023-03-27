# 경쟁적 전염
from collections import deque
import sys
f = sys.stdin.readline

n, k = map(int, input().split())

graph = []
viruses = []
for i in range(n):
    graph.append(list(map(int, f().rstrip().split())))
    for j in range(n):
        if (graph[i][j] != 0):
            # 바이러스 번호, x, y, 시간초
            viruses.append((graph[i][j], i, j, 0))

target_s, target_x, target_y = map(int, input().split())

# 낮은 번호부터 해야하니까 정렬하고 큐에 넣기
viruses.sort(key=lambda x: x[0])
viruses = deque(viruses)


def spread(virus_n, nx, ny, s):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        x = dx[i] + nx
        y = dy[i] + ny
        if (x < 0 or y < 0 or x >= n or y >= n):
            continue
        if (graph[x][y] == 0):
            graph[x][y] = virus_n
            viruses.append((virus_n, x, y, s+1))


while (viruses):
    virus_n, nx, ny, s = viruses.popleft()
    # 처음 나오는 애의 s가 타겟s랑 같으면 딱 그 시간이 지난 거임
    if (target_s == s):
        break
    spread(virus_n, nx, ny, s)

print(graph[target_x-1][target_y-1])
