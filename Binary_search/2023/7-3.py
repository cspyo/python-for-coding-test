# 떡볶이 떡 만들기

import sys
f = sys.stdin.readline

n, m = map(int, input().split())
rice_cakes = list(map(int, f().rstrip().split()))

rice_cakes.sort()


def sum_length_of_cakes(x):
    length_of_cakes = 0
    for i in rice_cakes:
        if (i > x):
            length_of_cakes += (i-x)
    return length_of_cakes


def binary_search():
    start = 0
    end = max(rice_cakes)
    mid = 0
    while (start <= end):
        mid = (start+end)//2
        length_of_cakes = sum_length_of_cakes(mid)
        if (length_of_cakes == m):
            return mid
        elif (length_of_cakes < m):
            end = mid-1
        else:
            start = mid+1
    return mid


print(binary_search())
