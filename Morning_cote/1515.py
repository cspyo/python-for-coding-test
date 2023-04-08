# 수 이어 쓰기
# https://www.acmicpc.net/problem/1515

arr = list(map(int, input()))


def solution(arr):
    pointer = 0
    base = 1
    while True:
        for item in str(base):
            if (arr[pointer] == int(item)):
                pointer += 1
            if (pointer == len(arr)):
                return base
        base += 1


print(solution(arr))
