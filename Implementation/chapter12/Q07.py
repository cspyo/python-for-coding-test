# 럭키 스트레이트

n = input()

length = len(n)
half=length/2
left=0
right=0
for i in range(length):
    if i<half:
        left+=int(n[i])
    else:
        right+=int(n[i])

if left==right:
    print("LUCKY")
else:
    print("READY")