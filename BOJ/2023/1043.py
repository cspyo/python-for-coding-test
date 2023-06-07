import sys
input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
history = []

know_the_truth = list(map(int, input().split()))[1:]
for i in know_the_truth:
    parent[i] = 0

for i in range(1, m+1):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]
    history.append(party)
        
    for i in range(party_len - 1):
        union(parent, party[i], party[i+1])


answer = 0
for i in range(m):
    for a in history[i]:
        if parent[find(parent, a)] == 0:
            answer+=1
            break
        

print(m-answer)
    
