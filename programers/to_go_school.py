# 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 다이나믹 프로그래밍

def solution(m, n, puddles):
    # 좌표를 (m, n)이라고 하는데 행 열로 표현하면 (n, m)이다. 주의하기

    # DP 테이블 -1로 전부 초기화
    dp_table = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    # 시작 지점인 (1,1)은 1로 초기화
    dp_table[1][1] = 1

    # 물이 잠긴 곳은 0으로 초기화
    for i, j in puddles:
        dp_table[j][i] = 0

    # 왼쪽 위 제로 패딩
    for i in range(m+1):
        dp_table[0][i] = 0
    for j in range(n+1):
        dp_table[j][0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            # 시작 지점은 패스
            if i == 1 and j == 1:
                continue
            # 물이 잠긴 곳도 패스
            if dp_table[i][j] == 0:
                continue
            # (i, j) 의 값은 (i-1, j)+(i, j-1) 이다
            else:
                dp_table[i][j] = (dp_table[i-1][j] +
                                  dp_table[i][j-1]) % 1000000007

    answer = dp_table[n][m]
    return answer
