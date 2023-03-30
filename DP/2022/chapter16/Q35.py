# 못생긴 수
# d[i/2, i/3, i/5]==True , d[i]=True

n=int(input())

dp=[False]*(30001)
dp[1], dp[2], dp[3], dp[5] = True, True, True, True
for i in range(1, 30001):
    if i%2==0:
        if dp[i//2]==True:
            dp[i]==True
    if i%3==0:
        if dp[i//3]==True:
            dp[i]==True
    if i%5==0:
        if dp[i//5]==True:
            dp[i]==True

count=0
while count<n:
    for i in range(30001):
        if dp[i]==True:
            count+=1

print(count)


