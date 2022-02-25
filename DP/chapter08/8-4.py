# 효율적인 화폐 구성

INF = 10001
n, m = map(int, input().split())
hwape = []
for _ in range(n):
    hwape.append(int(input()))


d=[INF] * (m+1)
d[0]=0

for h in hwape:
    for i in range(h, m+1):
        if d[i-h]!=INF:
            d[i] = min(d[i], d[i-h]+1)

if d[m]==INF:
    print(-1)
else:
    print(d[m])