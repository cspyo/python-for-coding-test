# 문자열 재정렬

import heapq

arr = input()


def solution(arr):
    answer = ''
    min_heap = []
    sum_num = 0
    for item in arr:
        if not item.isdecimal():
            heapq.heappush(min_heap, item)
        else:
            sum_num += int(item)
    while min_heap:
        a = heapq.heappop(min_heap)
        answer += a
    answer += str(sum_num)
    return answer


print(solution(arr))
