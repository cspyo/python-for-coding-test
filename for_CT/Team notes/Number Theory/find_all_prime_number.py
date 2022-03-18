# n보다 작거나 같은 모든 소수 찾기
# 에라토스테네스의 체

import math

n=1000
array=[True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i]==True:
        j=2
        while i*j <= n:
            array[i*j]=False
            j+=1

for i in range(2, n+1):
    if array[i]:
        print(i, end=" ")