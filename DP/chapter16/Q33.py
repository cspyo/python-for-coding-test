# 퇴사
# BOJ 14501

n = int(input())
data=[(0,0)]
for _ in range(n):
    t,p = map(int, input().split())
    data.append((t,p))

dp = [0] *(n+2)


for i in range(1,n+1):
    if i+data[i][0]<=n+1:
        dp[i+data[i][0]] = max(dp[i+data[i][0]], data[i][1]+dp[i])
        for j in range(i+data[i][0], n+2):
            #dp[j] = max(dp[i+data[i][0]], dp[j])
            dp[j] = dp[i+data[i][0]]


print(max(dp))