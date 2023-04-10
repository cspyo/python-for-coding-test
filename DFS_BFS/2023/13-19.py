# 연산자 끼워 넣기
# https://www.acmicpc.net/problem/14888
# 브루트 포스

from itertools import permutations
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
# +, -, *, //
operators = list(map(int, input().split()))

INF = 1e9


def cal(arr, pick):
    q_num = deque(arr)
    q_pick = deque(pick)

    result = q_num.popleft()

    while q_num:
        num = q_num.popleft()
        operator = q_pick.popleft()

        if operator == 0:
            result += num
        elif operator == 1:
            result -= num
        elif operator == 2:
            result *= num
        else:
            if result < 0:
                result *= -1
                result //= num
                result *= -1
            else:
                result //= num
    return result


def solution(n, arr, operators):
    answer_min = INF
    answer_max = -INF

    for_permutations = []
    for i in range(4):
        for _ in range(operators[i]):
            for_permutations.append(i)

    picks = list(permutations(for_permutations, len(for_permutations)))

    for pick in picks:
        result = cal(arr, pick)
        answer_min = min(answer_min, result)
        answer_max = max(answer_max, result)

    print(answer_max)
    print(answer_min)


solution(n, arr, operators)
