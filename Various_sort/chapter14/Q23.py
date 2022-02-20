# 국영수
# BOJ 10825

import sys
f = sys.stdin.readline

n = int(f())
data=[]
for _ in range(n):
    name, k, e, m = f().split()
    data.append((int(k),int(e),int(m),name))

data.sort(key = lambda x : (-x[0],x[1],-x[2],x[3]))

for k,e,m,name in data:
    print(name)