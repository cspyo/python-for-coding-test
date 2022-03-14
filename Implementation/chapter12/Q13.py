# 치킨 배달
# BOJ 15686
from itertools import combinations

n, m = map(int, input().split())
house=[]
chicken=[]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j]==1:
            house.append((i, j))
        elif a[j]==2:
            chicken.append((i, j))

def distance(h, c):
    return abs(h[0]-c[0]) + abs(h[1]-c[1])

choose_chic = list(combinations(chicken, m))
result=int(1e9)
for choose in choose_chic:
    all_c=0
    for h in house:
        c_distance=int(1e9)
        for c in choose:
            c_distance=min(c_distance, distance(h, c))
        all_c+=c_distance
    result=min(result, all_c)

print(result)





