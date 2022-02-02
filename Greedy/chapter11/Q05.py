# 볼링공 고르기 내 소스코드

n,m = map(int, input().split())
data = list(map(int, input().split()))

# #my solution_slow
data.sort()
count=0
for i in range(n):
  for j in range(i+1,n):
    if data[i]!=data[j]:
      count+=1

print(count)