# 공유기 설치

# 도저히 모르겠어서 해답 봄
# (가장 인접한 두 공유기 사이의 거리) 를 이진탐색으로 탐색하는 것임
# gap을 이진탐색으로 설정하고 공유기를 앞에서부터 gap에 맞게 설치
# 설치한 공유기 개수가 c 값 이상인지 확인
# 이상이면 gap을 늘리고 c 값 미만이면 gap을 줄인다

import sys
f=sys.stdin.readline

n, c = map(int, input().split())

data=[]
for _ in range(n):
    data.append(int(f().rstrip()))
data.sort()


def install_wifi(gap):
    install=data[0]
    wifi=1
    for d in data:
        if d>=(install+gap):
            wifi+=1
            install=d
    return wifi

start=1
end=data[-1]-data[0]
result=0
while start<=end:
    gap = (start+end)//2
    if install_wifi(gap)<c:
        end=gap-1
    else:
        result=gap
        start=gap+1

print(result)

