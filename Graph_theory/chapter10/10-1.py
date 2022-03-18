# 팀 결성
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
parent = [0] * (n+1)

for i in range(n+1):
    parent[i]=i

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper==0:
        union_parent(parent, a, b)
    else:
        if parent[a]==parent[b]: # 이미 개선된 거라서 parent에 루트 노드가 다 들어있음
            print("YES")
        else:
            print("NO")
