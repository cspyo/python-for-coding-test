# 컴백홈
# https://www.acmicpc.net/problem/1189

r, c, k = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input().strip()))

result = 0


def dfs(x, y, distance):
    global result
    # 집에 도달했는데
    if ((x, y) == (0, c-1)):
        # 거리가 k라면 가짓수 +1
        if (distance == k):
            result += 1
            return
        else:
            return
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= nx < r and 0 <= ny < c):
            if (graph[nx][ny] != 'T'):
                graph[nx][ny] = 'T'
                dfs(nx, ny, distance+1)
                # 백트래킹: 다시 돌아갔을 때 방문처리를 반드시 해제해줘야함
                graph[nx][ny] = '.'


# 시작자리 방문처리
graph[r-1][0] = 'T'
dfs(r-1, 0, 1)
print(result)
