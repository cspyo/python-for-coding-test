# 감시 피하기
# https://www.acmicpc.net/problem/18428
# 완전 탐색

from itertools import combinations

n = int(input())
jido = []
for _ in range(n):
    jido.append(input().split())


def recursion(count):
    global result, jido
    if count == 3:
        if check():
            result = "YES"
    else:
        for i in range(n):
            for j in range(n):
                if jido[i][j] == "X":
                    jido[i][j] = "P"
                    recursion(count+1)
                    jido[i][j] = "X"


def check():
    global teachers, jido
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 선생님이 있는 위치에서 bfs 실행
    for teacher in teachers:
        for i in range(4):
            nx, ny = teacher
            while 0 <= nx < n and 0 <= ny < n:
                # 기둥을 만나면 break
                if (jido[nx][ny] == "P"):
                    break
                # 학생을 만나면 숨기 실패
                if (jido[nx][ny] == "S"):
                    return False
                nx += dx[i]
                ny += dy[i]
    # for문이 다 지나면 숨기 성공
    return True


teachers = []
for i in range(n):
    for j in range(n):
        if (jido[i][j] == 'T'):
            teachers.append((i, j))
result = "NO"

recursion(0)

print(result)
