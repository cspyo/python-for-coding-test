# 금광
# 2차원 dp 테이블을 형성
# 가장 왼쪽에서 진행 현재 자리에 올 수 있는 값 중 최대치랑 지금 내 자리 값이랑 더해서 dp 테이블에 넣기
# 이러면 마지막 열에서의 최대값이 최대로 캘 수 있는 양임

def f(n, m, data):
    direction=[0,-1,1]
    dp=[[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = data[i][0]
    for j in range(1, m):
        for i in range(n):
            for a in direction:
                ni = i+a
                nj = j-1
                if 0<ni<n:
                    dp[i][j] = max(dp[i][j], dp[ni][nj])
            dp[i][j] += data[i][j]
    result=0     
    for i in range(n):
        result = max(result, dp[i][m-1])
    return result

for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    data=[]
    index=0
    for i in range(n):
        data.append(a[index:index+m])
        index+=m
    print(f(n, m, data))

