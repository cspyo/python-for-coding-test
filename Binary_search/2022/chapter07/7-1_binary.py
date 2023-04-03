import sys
f = sys.stdin.readline

def binary_search(arr, start, end, target):
    while start<=end:
        mid = (start+end) // 2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return None

n = int(f().rstrip())
all = list(map(int, f().rstrip().split()))
m = int(f().rstrip())
request = list(map(int, f().rstrip().split()))

for r in request:
    a = binary_search(all, 0, len(all)-1, r)
    if a==None:
        print("no", end=' ')
    else:
        print("yes", end=' ')