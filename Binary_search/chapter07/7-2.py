# 떡볶이 떡 만들기

# 결국 해답 봄
# 중요한건 절단기의 높이를 이진트리로 결정하는 것임
# 떡의 최대 높이가 10억이라

import sys
f = sys.stdin.readline

n, m = map(int, f().rstrip().split())
data = list(map(int, f().rstrip().split()))

def cal_sum(h):
    result=0
    for d in data:
        if d>h:
            result=result+d-h
    return result

start=0
end=max(data)
result=0
while start<=end:
    mid = (start+end)//2
    if cal_sum(mid)<m:
        end=mid-1
    else:
        result=mid
        start=mid+1

print(result)




