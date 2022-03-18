# 도시 분할 계획
# BOJ 1647

# 크루스칼 먼저 하고 최대 비용 간선 하나를 제거
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n, m = map(int, input().split())
parent=[0] * (n+1)

for i in range(n+1):
    parent[i]=i

edges=[]
result=0
max_cost=0
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        max_cost = cost
        result+=cost

print(result-max_cost)

