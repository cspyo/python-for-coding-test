# 바닥 공사
# BOJ 11727, 11726

n = int(input())

d = [0] * 1001

d[1]=1
d[2]=3

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]*2) % 10007

print(d[n])