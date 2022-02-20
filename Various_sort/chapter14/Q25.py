# 실패율
# 프로그래머스 42889

# 계수정렬 개념을 사용해서 풀었음
def solution(N, stages):
    count=[0] * (N+1+1)
    for i in stages:
        count[i]+=1

    data=[]
    for i in range(1, len(count)):
        if sum(count[i:])!=0:
            loss = count[i]/sum(count[i:])
            data.append((i, loss))
        else:
            data.append((i,0))

    answer = []
    data.sort(key=lambda x : (-x[1], x[0]))
    for d in data:
        if d[0]<=N:
            answer.append(d[0])
    return answer