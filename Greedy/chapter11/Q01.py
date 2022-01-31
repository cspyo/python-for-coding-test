# 모험가 길드

n = int(input())
group = list(map(int, input().split()))
group.sort()

result=0
count=0

for i in group:
  count+=1
  if count>=i:
    result+=1
    count=0

print(result)