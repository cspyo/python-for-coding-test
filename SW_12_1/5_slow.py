# 5번
# 14분걸리긴 해ㅔㅆ는데 이 풀이는 ㄹㅇ 개쌉느림 미쳤음 메모리도 안될거 같음

n=int(input())

ki=[[] for _ in range(100000000)]
for _ in range(n*n):
    data=list(map(int, input().split()))
    score=data[0]
    for a in data[2:]:
        ki[a].append(score)

result=0
for i in range(1, 100000000):
    if ki[i]:
        result+=max(ki[i])

print(result)