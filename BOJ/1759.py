# 암호 만들기
from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())

array = list(input().split())
array.sort()
print(array)
for password in combinations(array, l):
    count=0
    for i in password:
        if i in vowels:
            count+=1

    if count>=1 and count<=l-2:
        print(''.join(password))