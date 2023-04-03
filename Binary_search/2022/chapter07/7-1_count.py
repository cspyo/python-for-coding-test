# 부품 찾기
import sys
f = sys.stdin.readline

n = int(f().rstrip())
count = [0] * 1000001 
for i in list(map(int, f().rstrip().split())):
    count[i]+=1
m = int(f().rstrip())
request = list(map(int, f().rstrip().split()))


for r in request:
    if count[r]==0:
        print("no", end=' ')
    else:
        print("yes", end=' ')
