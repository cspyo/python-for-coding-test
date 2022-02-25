# 1,2,3 더하기
# DP 문제

def f(n):
    d=[0]*11
    d[1]=1
    d[2]=2
    d[3]=4
    for i in range(4,n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    
    return d[n]


t = int(input())
n=[]
for _ in range(t):
    n.append(int(input()))

for i in n:
    print(f(i))