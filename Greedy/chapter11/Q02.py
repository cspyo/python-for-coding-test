# 곱하기 혹은 더하기

# 1이하면 더하고 나머지는 다 곱하기
# 1도 더해야하는거 생각 못했음
s = input()

result=int(s[0])

for i in range(1,len(s)):
  a=int(s[i])
  if result<=1 or a<=1:
    result+=a
  else:
    result*=a

print(result)