# 백트래킹
# BOJ 14888
# 연산자 끼워넣기
# 줜나 느려서 pypy로 해야 통과임

from itertools import permutations
INF = int(1e9)

n=int(input())
data = list(map(int, input().split()))
op = list(map(int, input().split()))
for_permu=[]
for i in range(4):
    for j in range(op[i]):
        for_permu.append(i)

op_list = list(permutations(for_permu, n-1))

max_value=-INF
min_value=INF
for oper in op_list:
    
    i=0
    result=data[i]
    for o in oper:
        i+=1
        if o==0:
            result+=data[i]
        elif o==1:
            result-=data[i]
        elif o==2:
            result*=data[i]
        else:
            if result<0:
                result = -(abs(result)//data[i])
            else:
                result = (result//data[i])
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)