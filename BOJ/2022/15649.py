# 백트래킹이라네

from itertools import permutations

n, m = map(int, input().split())

data=[]
for i in range(1, n+1):
    data.append(i)

result = list(permutations(data, m))

for r in result:
    for a in r:
        print(a, end=" ")
    print()
