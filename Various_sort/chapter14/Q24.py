# 안테나
# BOJ 18310

n = int(input())
data = list(map(int, input().split()))

data.sort()

result = data[(n-1)//2]
print(result)