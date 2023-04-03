# 정렬된 배열에서 특정 수의 개수 구하기

from tkinter import W

n,x = map(int, input().split())
data = list(map(int, input().split()))

def find_first(start, end, target, arr):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            end=mid-1
            break
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    
    if start>end:
        return None

    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            result=mid
            end=mid-1
        elif arr[mid]<target:
            start=mid+1
    return result

def find_last(start, end, target, arr):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            start=mid+1
            break
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    
    if start>end:
        return None

    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            result=mid
            start=mid+1
        elif arr[mid]>target:
            end=mid-1
    return result


def count():
    f = find_first(0, n-1, x, data)
    if f==None:
        return 0
    l = find_last(0, n-1, x, data)

    result = l - f +1
    return result
    

print(count())