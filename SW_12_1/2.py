# 2번
# 18분
# 그리디네 남은 시간 안에서 가장 큰거만 고르는

p,n,h = map(int, input().split())
data=[[] for _ in range(p+1)]
for _ in range(n):
    x,y = map(int, input().split())
    if y<h:
        data[x].append(y)

result=[0]
for i in range(1,p+1):
    if not data[i]:
        result.append(0)
    else:
        data[i].sort(reverse=True)
        now_h=h
        price=0
        for a in data[i]:
            if a>now_h:
                continue
            price+=a*1000
            now_h-=a
        result.append(price)

for i in range(1, p+1):
    print(i, result[i])





