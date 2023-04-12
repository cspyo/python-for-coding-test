# 감시 피하기
# https://www.acmicpc.net/problem/18428
# 완전 탐색

from itertools import combinations

n = int(input())
jido = []
for _ in range(n):
    jido.append(input().split())


# 감시하기
def check(teachers, jido):
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


def solution(jido):
    # 선생님의 위치와 빈 공간 저장
    empty_places = []
    teachers = []
    for i in range(n):
        for j in range(n):
            if (jido[i][j] == 'X'):
                empty_places.append((i, j))
            elif (jido[i][j] == 'T'):
                teachers.append((i, j))
    # 빈 공간에서 기둥 놓을 위치 세 곳을 순서 상관없이 중복 안되게 뽑기
    pillars = list(combinations(empty_places, 3))

    # 기둥을 놓고
    for pillar in pillars:
        jido_tmp = [item[:] for item in jido]
        for (x, y) in pillar:
            jido_tmp[x][y] = 'P'
        # 세 기둥을 다 놓고 숨기 성공했는지 check
        if check(teachers, jido_tmp):
            return "YES"
    return "NO"


print(solution(jido))
