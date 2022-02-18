# 음료수 얼려먹기

n, m = map(int, input().split())
ice =[]
for _ in range(n):
    ice.append(list(map(int, input())))

def dfs(x,y):
    if x<0 or x>m or y<0 or y>n:
        return False
    if ice[x][y]==0:
        ice[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
    
# 내 상하좌우에서 0인곳 1로 만들고 처음 나 자신은 True가 반환됨
# 내가 1이면 False가 됨
# 그림을 그려보면 이해가 빠름
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)