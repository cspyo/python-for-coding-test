# 미로 탈출
from collections import deque
import sys
f = sys.stdin.readline

n, m = map(int, f().rstrip().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, f().rstrip())))

# now = (0, 0)
# end = (n-1, m-1)

queue = deque()
queue.append((0, 0))

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

while (len(queue) != 0):
    x, y = queue.popleft()
    for i in range(4):
        now_x = x+move_x[i]
        now_y = y+move_y[i]
        if (now_x < 0 or now_y < 0 or now_x >= n or now_y >= m):
            continue
        if (miro[now_x][now_y] == 0):
            continue
        if (miro[now_x][now_y] == 1):
            miro[now_x][now_y] = miro[x][y]+1
            queue.append((now_x, now_y))


print(miro[n-1][m-1])
