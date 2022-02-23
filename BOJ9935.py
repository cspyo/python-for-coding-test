# BOJ 9935 문자열 폭발

data = input()
bomb = input()

remain=[]
l = len(bomb)
for s in data:
    remain.append(s)
    if "".join(remain[-l:])==bomb:
        remain[-l:]=[]

if remain:
    print("".join(remain))
else:
    print("FRULA")