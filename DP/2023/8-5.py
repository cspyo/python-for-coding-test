# 효율적인 화폐 구성

n, m = map(int, input().split())


INF = 10001
d = [INF]*(10001)
bills = []

for _ in range(n):
    bill = int(input())
    d[bill] = 1
    bills.append(bill)

for i in range(min(bills), m+1):
    min_value = d[i]
    for bill in bills:
        min_value = min(min_value, d[i-bill]+1)
    d[i] = min_value

if (d[m] == 10001):
    print(-1)
else:
    print(d[m])
