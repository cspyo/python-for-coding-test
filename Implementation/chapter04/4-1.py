# 상하좌우

n = int(input())
data = list(map(str, input().split()))

x, y = 1, 1
for a in data:
    if a=="L":
        if x>1:
            x-=1
    elif a=="R":
        if x<n:
            x+=1
    elif a=="U":
        if y>1:
            y-=1   
    else:
        if y<n:
            y+=1

print(y, x)