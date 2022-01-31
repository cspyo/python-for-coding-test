d=[]
for i in range(10):
    d.append([])

for i in range(10):
    a = input().split()
    for v in a:
        d[i].append(int(v))

m=1
n=1

while True:
    d[m][n]=9
    if not d[m][n+1] or d[m][n+1]==2:
        n+=1
    elif not d[m+1][n] or d[m+1][n]==2:
        m+=1
    else:
        break

    if d[m][n]==2:
        d[m][n]=9
        break

for i in range(10):
    for j in range(10):
        print(d[i][j], end=" ")
    print()

