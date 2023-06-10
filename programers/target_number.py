# 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
# 완전 탐색

from itertools import product


def solution(numbers, target):
    answer = 0
    picks = list(product([0, 1], repeat=len(numbers)))
    for pick in picks:
        result = 0
        for i in range(len(numbers)):
            if pick[i] == 0:
                result += numbers[i]
            else:
                result -= numbers[i]

        if result == target:
            answer += 1

    return answer


print(solution([1, 1, 1, 1, 1], 3))
