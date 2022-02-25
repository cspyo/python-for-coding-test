# 개미 전사

n = int(input())
data = list(map(int, input().split()))


dp_table=[0] * (100)
dp_table[0] = data[0]
dp_table[1] = max(data[0], data[1])

for i in range(2, n+1):
    dp_table[i] = max(dp_table[i-1], dp_table[i-2]+data[i])

print(dp_table[n-1])