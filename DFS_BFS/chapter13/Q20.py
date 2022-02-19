# 감시 피하기
# BOJ 18428

# 일단 이것도 조합 이용해서 3개 장애물 설치의 모든 경우의 수 따져봐야할듯
# 들킨다는 기준 = 선생 기준으로 십자만 다 보면 되잖아

from itertools import combinations
import sys
f = sys.stdin.readline

n = int(f())
data=[]
for _ in range(n):
    data.append(list(f().split()))
tmp_data = [item[:] for item in data]
can_make_stuff = []
teacher=[]
for i in range(n):
    for j in range(n):
        if data[i][j]=='X':
            can_make_stuff.append((i,j))
        elif data[i][j]=='T':
            teacher.append((i,j))


def find_student(x,y):
    nx=x
    ny=y
    while nx>=0:
        if tmp_data[nx][ny]=='S':
            return True
        elif tmp_data[nx][ny]=='O':
            break
        nx-=1
    nx=x
    ny=y
    while nx<n:
        if tmp_data[nx][ny]=='S':
            return True
        elif tmp_data[nx][ny]=='O':
            break
        nx+=1
    nx=x
    ny=y
    while ny>=0:
        if tmp_data[nx][ny]=='S':
            return True
        elif tmp_data[nx][ny]=='O':
            break
        ny-=1
    nx=x
    ny=y
    while ny<n:
        if tmp_data[nx][ny]=='S':
            return True
        elif tmp_data[nx][ny]=='O':
            break
        ny+=1
    return False

for stuff in combinations(can_make_stuff, 3):
    # 장애물 설치
    stuff=list(stuff)
    for x,y in stuff:
        tmp_data[x][y]='O'
    
    a=0
    # 학생 찾기
    for x,y in teacher:
        if find_student(x,y):
            a+=1
    
    if a==0:
        break

    # 맵 다시 복구
    for x,y in stuff:
        tmp_data[x][y]='X'
    
if a==0:
    print("YES")
else:
    print("NO")