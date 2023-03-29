# 백트래킹

from itertools import combinations_with_replacement

n, m = map(int, input().split())

data=[]
for i in range(1, n+1):
    data.append(i)

result = list(combinations_with_replacement(data, m))

for r in result:
    for a in r:
        print(a, end=" ")
    print()
