# 큰 수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/42883?language=python3


# 시간초과 코드
from itertools import combinations

INF = int(1e9)
def solution(number, k):
    answer = ''
    n = len(number)
    indexs = list(range(n))
    pick = combinations(indexs, n-k)
    max_value = -INF
    for item in pick:
        new_number = ''
        for i in item:
            new_number += number[i]
            if int(new_number) > max_value:
                max_value = int(new_number)
                answer = new_number
                
    return answer