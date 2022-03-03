# 5번 다시
# 빠르게 만들었당
from collections import deque

n = int(input())
q=[]
for _ in range(n*n):
    data=list(map(int, input().split()))
    for a in data[2:]:
        q.append((a,data[0]))

q.sort()
q=deque(q)
n=1
result=0
max_value=0
while q:
    sec, score = q.popleft()
    if n==sec:
        max_value = max(max_value, score)
    else:
        n=sec
        result+=max_value
        max_value=score
result+=score
print(result)