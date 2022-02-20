array = [5,7,9,0,3,1,6,2,4,8]

## 정석
def quick_sort_1(array, start, end):
    if start>=end:
        return
    
    pivot = start
    left = start+1
    right = end

    while left<=right:
        while left<=end and array[pivot]<=array[left]:
            left+=1
        while right>=start+1 and array[pivot]>array[right]:
            right-=1
        if left>right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort_1(array, start, right-1)
    quick_sort_1(array, right+1, end)

## 파이써닉
def quick_sort_2(array):
    if len(array)==1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_array = [x for x in tail if x<=pivot]
    right_array = [x for x in tail if x>pivot]

    return quick_sort_2(left_array) + [pivot] + quick_sort_2(right_array)


