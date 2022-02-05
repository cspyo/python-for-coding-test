from collections import deque
n = int(input())
# 벽 또는 자기 자신
# 일단 맵부터 만들자
# out of index되면 귀찮으니까 그냥 다 늘려서 만들자
# [0]이랑 [n+1]은 벽 2로 초기화
# 나 자신도 2로
board = [[0] * (n+2) for _ in range(n+2)]
for i in range(n+2):
    board[i][0]=2
    board[i][n+1]=2
    board[n+1][i]=2
    board[0][i]=2

k = int(input())
for _ in range(k):
    x,y = map(int, input().split())
    board[x][y]=1

l = int(input())
info=deque([])
for _ in range(l):
    s,c = input().split()
    info.append((int(s),c))


# 동 남 서 북 순으로(오 아래 왼 위)
d = 0
direction_list = [(0,1), (1,0), (0,-1), (-1,0)]
snake=deque([(1,1)])
board[snake[0][0]][snake[0][1]]=2
count = 0

while True:
    n_x = snake[0][0] + direction_list[d][0]
    n_y = snake[0][1] + direction_list[d][1]
    snake.appendleft((n_x,n_y))
    count+=1
    if board[n_x][n_y]==2:
        print(count)
        break
    elif board[n_x][n_y]==0:
        board[n_x][n_y]=2
        tmp=snake.pop()
        board[tmp[0]][tmp[1]] = 0
    elif board[n_x][n_y]==1:
        board[n_x][n_y]=2
    if info:
        if count==info[0][0]:
            if info[0][1]=='L':
                d = (d-1) % 4
            elif info[0][1]=='D':
                d = (d+1) % 4
            info.popleft()
