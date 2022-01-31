# 큰 수의 법칙

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

sum=0
# while True:
#   for _ in range(k):
#     if m==0:
#       break
#     sum+=first
#     m-=1
#   if m==0:
#       break    
#   sum+=second
#   m-=1

sum = sum + first*(m//(k+1)*k) + first*(m%(k+1))
sum = sum + second*(m//(k+1))  

print(sum)
    