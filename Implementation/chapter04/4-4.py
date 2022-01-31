# 게임 개발

n, m = map(int, input().split())
x, y, d = map(int, input().split())
field=[]
for _ in range(n):
    row = list(map(int, input().split()))
    field.append(row)

move = [(-1,0), (0,1), (1,0), (-1,0)]

rcount=0
result=1
while True:
    field[x][y]=2
    d-=1
    if d<0:
        d=3
    rcount+=1

    nx = x+move[d][0]
    ny = y+move[d][1]
    if not field[nx][ny]:
        x, y = nx, ny
        rcount=0
        result+=1
    elif field[nx][ny]==2 and rcount==4:
        x, y = nx, ny
        rcount=0
        continue
    elif field[nx][ny]==1 and rcount==4:
        break
    
print(result)


