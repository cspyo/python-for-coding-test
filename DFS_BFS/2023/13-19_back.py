# 연산자 끼워 넣기
# https://www.acmicpc.net/problem/14888
# 백트래킹


n = int(input())
arr = list(map(int, input().split()))
# +, -, *, //
add, sub, mul, div = list(map(int, input().split()))

INF = 1e9

answer_min = INF
answer_max = -INF


def recursion(now, result):
    global answer_max, answer_min
    global add, sub, mul, div

    if now == n:
        answer_max = max(answer_max, result)
        answer_min = min(answer_min, result)
    else:
        if add > 0:
            add -= 1
            recursion(now+1, result+arr[now])
            add += 1
        if sub > 0:
            sub -= 1
            recursion(now+1, result-arr[now])
            sub += 1
        if mul > 0:
            mul -= 1
            recursion(now+1, result*arr[now])
            mul += 1
        if div > 0:
            div -= 1
            if result < 0:
                recursion(now+1, -(abs(result)//arr[now]))
            else:
                recursion(now+1, result//arr[now])
            div += 1


def solution(n, arr):
    recursion(1, arr[0])

    print(answer_max)
    print(answer_min)


solution(n, arr)
