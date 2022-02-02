# 문자열 재정렬

s = input()

s_list=[]
num_list=[]

for i in range(len(s)):
    if ord(s[i])%48<10:
        num_list.append(int(s[i]))
    else:
        s_list.append(s[i])

s_list.sort()
for a in s_list:
    print(a, end="")
print(sum(num_list))