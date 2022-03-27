# 소수 구하기
# 에라토스테네스의 체 사용

import math

m, n = map(int, input().split())
array = [True for i in range(n+1)]

array[1] = 0

for i in range(2, int(math.sqrt(n))+1):
    if array[i]==True:
        j=2
        while i*j <= n:
            array[i*j] = False
            j+=1

for i in range(m, n+1):
    if array[i]:
        print(i)