# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선 개수 입력
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

# 간선들의 비용 정보 넣기
edges = []
result=0
for _ in range(e):
    a, b, cost= map(int, input().split())
    edges.append((cost, a, b))

# 크루스칼 알고리즘을 위한 간선 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = cost
    # 사이클이 발생하지 않으면 유니온
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost

print(result)
