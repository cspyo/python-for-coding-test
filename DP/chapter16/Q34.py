# 병사 배치하기
# BOJ 18353

# 가장 긴 증가하는 부분 수열
# 0<=j<i, d[i] = max(d[i],d[j]+1) if array[j]<array[i]




n=int(input())
data=list(map(int, input().split()))

data.reverse()

dp=[1]*(n)

for i in range(1, n):
    for j in range(i):
        if data[j]<data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))


            
