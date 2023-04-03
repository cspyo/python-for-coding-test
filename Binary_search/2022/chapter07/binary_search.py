
def binary_search(arr, data, start, end):
    while start<=end:
        mid = (start+end) // 2
        
        if arr[mid]==data:
            return mid
        elif arr[mid]>data:
            end=mid-1
        else:
            start=mid+1
    return None



arr = [0,2,4,6,8,10,12,14,16,18]

print(binary_search(arr, 4, 0, 9))


