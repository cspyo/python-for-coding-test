# 배열 복원하기
# https://www.acmicpc.net/problem/16967

import sys
f = sys.stdin.readline

h, w, x, y = map(int, input().split())
b = []
for _ in range(h+x):
    b.append(list(map(int, f().rstrip().split())))

a = [[0 for _ in range(w+y)] for _ in range(h+x)]
for i in range(h+x):
    for j in range(w+y):
        if (i < x or j < y):
            a[i][j] = b[i][j]
        elif (i > h or j > w):
            a[i-x][j-y] = b[i][j]
        elif (x <= i < h and y <= j < w):
            a[i][j] = b[i][j]-a[i-x][j-y]

for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()
