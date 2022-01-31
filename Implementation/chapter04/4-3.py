# 왕실의 나이트

a = input()

x=int(a[1]) # 숫자는 그대로 정수로
y=ord(a[0])%96 # 문자는 a가 97이다. 체스판에서 a는 1을 가르키므로 96으로 나머지 계산해준다.

move_type = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]

count=0
for move in move_type:
    nx = x + move[0]
    ny = y + move[1]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    else:
        count+=1

print(count)