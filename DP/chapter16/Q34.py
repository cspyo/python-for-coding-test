# 병사 배치하기
# BOJ 18353


def naerim(arr, now):
    prev=arr[0]
    count=1
    for i in range(1, len(arr)):
        if prev>arr[i]>now:
            count+=1
            prev=arr[i]
    
    return count+1

n=int(input())
data=list(map(int, input().split()))


a=[15,11,4,8,5,2,4]
dp=[1]*(n+1)


for i in range(1,n):
    dp[i] = naerim(a[:i], a[i])

print(dp)

            
