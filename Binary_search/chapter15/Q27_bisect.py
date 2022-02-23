# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

n,x = map(int, input().split())
data = list(map(int, input().split()))

left_index = bisect_left(data, x)
right_index = bisect_right(data, x)

print(-1 if (right_index-left_index)==0 else right_index-left_index)
