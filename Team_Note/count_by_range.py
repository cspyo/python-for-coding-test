from bisect import bisect_left, bisect_right

## left_value <= x <= right_value 의 개수 반환
def count_by_range(array, left_value, right_value):
    right = bisect_right(array, right_value)
    left = bisect_left(array, left_value)
    return right-left



array = [1,2,3,3,3,3,3,3,4,4,8,9]
print(count_by_range(array, -1,3))