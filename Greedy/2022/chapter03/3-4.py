# 1이 될 때까지

n,k = map(int, input().split())

result=0

result+=n%k
while n!=1:
  n=n//k
  result+=1

print(result)