# 정수 삼각형
# BOJ 1932

n = int(input())
data=[]
for _ in range(n):
    d = list(map(int, input().split()))
    data.append(d)

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            left=0
            right=data[i-1][j]
        elif j==i:
            left=data[i-1][j-1]
            right=0
        else:
            left=data[i-1][j-1]
            right=data[i-1][j]
        data[i][j] = data[i][j] + max(left, right)

print(max(data[n-1]))
