# 붐버맨
# https://www.acmicpc.net/problem/16918

import sys
f = sys.stdin.readline

r, c, n = map(int, f().split())

# 빈 곳은 4
# 나머지는 폭탄
# 폭탄은 0초가 되면 터짐


def make_map(item):
    if (item == '.'):
        return 5
    else:
        return 3


bomb_map = []
for i in range(r):
    bomb_map.append(list(map(make_map, f().rstrip())))


def bomb(nx, ny):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        x = dx[i] + nx
        y = dy[i] + ny
        if (x < 0 or y < 0 or x >= r or y >= c):
            continue
        bomb_map[x][y] = 4


bomb_list = []
for _ in range(n):
    for i in range(r):
        for j in range(c):
            bomb_map[i][j] -= 1
            if (bomb_map[i][j] == 0):
                bomb_list.append((i, j))
                # 여기서 bomb()을 돌리면 원래 0이였던 곳의 폭탄이 안터짐
                # 그래서 이 시간에 터지는 폭탄의 리스트를 만들고
    # 한 번에 터트리기
    while (bomb_list):
        nx, ny = bomb_list.pop()
        bomb_map[nx][ny] = 4
        bomb(nx, ny)

for row in bomb_map:
    for item in row:
        if (item == 4):
            print('.', end='')
        else:
            print('O', end='')
    print()
