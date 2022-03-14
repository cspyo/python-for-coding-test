# 3번
# 26분정도 걸림 왜케 오래걸림..
# 심지어 틀림
# 먼저 잘 구상해야할듯
# 내가 움직인 거리의 최소가 아니라 빨간 선의 최소
# 이미 그려진 빨간 선을 움직이는 건 길이 안늘어남
# 그니까 그냥 처음 위치에서 모든 땅콩과의 거리 구해서 튜플로 리스트에 저장하고 정렬

# 그리디네

INF = int(1e9)
n,m,e = map(int, input().split())
data = list(map(int, input().split()))
dist=[]
for i in data:
    dist.append((i, abs(e-i)))

dist.sort(key=lambda x: x[1])
print(dist)
ate_l=[]
ate=0
for a in dist:
    ate_l.append(a[0])
    ate+=1
    if ate==m:
        break

print(max(ate_l)-min(ate_l))


