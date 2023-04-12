# 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
# 백트래킹

answer = 0


def recursion(cnt, result, numbers, target, n):
    global answer
    if cnt == n:
        if result == target:
            answer += 1
    else:
        recursion(cnt+1, result-numbers[cnt], numbers, target, n)
        recursion(cnt+1, result+numbers[cnt], numbers, target, n)


def solution(numbers, tg):
    global answer, target, n
    n = len(numbers)
    target = tg

    recursion(0, 0, numbers, target, n)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
