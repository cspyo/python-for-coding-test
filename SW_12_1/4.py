# 4번
# 9분

n = int(input())
data = list(map(int, input().split()))

visited=[False]*n

def sol(start):
    count=1
    now=start
    while not visited[now]:
        count+=1
        visited[now]=True
        now+=data[now]
    return count

result=0
for i in range(3):
    result = max(result, sol(i))

print(result)