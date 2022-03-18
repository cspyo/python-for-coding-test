# 1번
# 거의 40~50분
skill_list = list(input().split())

graph=[[] for _ in range(len(skill_list))]

n = int(input())
for _ in range(n):
    x, y = input().split()
    a = skill_list.index(x)
    b = skill_list.index(y)
    graph[a].append(b)

stack=[]
stack.append((0,[0]))

## dfs를 이용해서 경로를 저장
result=[]
while stack:
    a, path = stack.pop()
    if not graph[a]:
        result.append(path)
    else:
        for v in graph[a]:
            stack.append((v, path+[v]))

for a in reversed(result):
    for i in a:
        print(skill_list[i], end=" ")
    print()



