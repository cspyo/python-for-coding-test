# N-Queen
# https://www.acmicpc.net/problem/9663
# 백트래킹

n = int(input())

# is_queen[0]=1 이면 (0,1)에 퀸이 존재
is_queen = [0]*n
result = 0


def check(i):
    # 왼쪽 위부터 퀸을 놓으니까 아래 오른쪽은 안봐도 된다
    for x in range(i):
        # 같은 열에 퀸이 있거나 or 대각선에 있으면
        if (is_queen[i] == is_queen[x] or abs(is_queen[i]-is_queen[x]) == abs(i-x)):
            return False
    return True


def queen(i):
    global result
    # n번째 줄(인덱스n-1)까지 전부 퀸을 놓았다면 +1
    if (i == n):
        result += 1
        return
    for j in range(n):
        is_queen[i] = j
        if (check(i)):
            queen(i+1)


queen(0)
print(result)
