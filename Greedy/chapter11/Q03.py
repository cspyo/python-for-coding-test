# 문자열 뒤집기

# 처음을 기준으로 숫자가 두번 바뀌면 1번 연산
# 다해서 홀수이면 +1해서 2로 나누면 될듯

s=input()
now=s[0]
count=0
for i in range(1,len(s)):
  if now != s[i]:
    count+=1
  now=s[i]

if count%2==0:
  print(count//2)
else:
  print((count//2) +1)



# 요거 지린다이
# S = input()
# a = S.count('01')
# b = S.count('10')
# print(max(a,b))