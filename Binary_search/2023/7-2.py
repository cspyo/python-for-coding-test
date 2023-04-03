# 부품 찾기

import sys
f = sys.stdin.readline


n = int(f().rstrip())
store = list(map(int, f().rstrip().split()))
m = int(f())
request = list(map(int, f().rstrip().split()))


def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while (start <= end):
        mid = (start+end)//2
        if (arr[mid] == target):
            return mid
        elif (arr[mid] > target):
            end = mid-1
        else:
            start = mid+1
    return None


store.sort()


for item in request:
    if (binary_search(store, item) == None):
        print("No")
    else:
        print("Yes")
