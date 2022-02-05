from collections import deque

# 맵 만들기
n = int(input())
board = [[0] * (n+2) for _ in range(n+2)]
for i in range(n+2):
    board[i][0]=2
    board[i][n+1]=2
    board[n+1][i]=2
    board[0][i]=2

# 사과 놓기
k = int(input())
for _ in range(k):
    x,y = map(int, input().split())
    board[x][y]=1

# 방향 정보 삽입
l = int(input())
info=deque([])
for _ in range(l):
    s,c = input().split()
    info.append((int(s),c))

# 동 남 서 북 순으로(오 아래 왼 위)
d = 0
direction_list = [(0,1), (1,0), (0,-1), (-1,0)]
snake=deque([(1,1)])
count = 0

while True:
    x=snake[0][0]
    y=snake[0][1]
    board[x][y]=2
    n_x = x + direction_list[d][0]
    n_y = y + direction_list[d][1]
    snake.appendleft((n_x,n_y))
    count+=1
    # 벽이거나 나 자신을 만나면 끝
    if board[n_x][n_y]==2:
        print(count)
        break
    # 사과 없으면 꼬리 지우기 있으면 늘어난 상태로 진행
    elif board[n_x][n_y]==0:
        tmp=snake.pop()
        board[tmp[0]][tmp[1]] = 0
    # 방향 바꾸기
    if info:
        if count==info[0][0]:
            if info[0][1]=='L':
                d = (d-1) % 4
            elif info[0][1]=='D':
                d = (d+1) % 4
            info.popleft()
