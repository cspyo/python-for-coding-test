# 문자열 재정렬

data = input()
s_list = []
sum = 0

for x in data:
    if x.isalpha():
        s_list.append(x)
    else:
        sum+=int(x)

s_list.sort()

if sum!=0:
    s_list.append(str(sum))

print("".join(s_list))

