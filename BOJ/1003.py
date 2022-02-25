# 피보나치 함수
# DP 문제


def f(n):
    d=[[0]*2 for _ in range(41)]
    d[0]=[1,0]
    d[1]=[0,1]
    for i in range(2, n+1):
        d[i] = [d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1]]
    
    return d[n]

t = int(input())
n=[]
for _ in range(t):
    n.append(int(input()))

for i in range(t):
    result = f(n[i])
    print(result[0], result[1])