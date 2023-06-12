# 시리얼 번호
# https://www.acmicpc.net/problem/1431

import sys
input = sys.stdin.readline

n = int(input())

serials = []
for _ in range(n):
    serials.append(input().rstrip())
    
for row in serials:
    print(row)

def sum_nums(x):
    sum = 0
    for c in x:
        if c.isdigit():
            sum+=int(c)
    return sum
    

sorted_list = sorted(serials, key=lambda x: (len(x), sum_nums(x), x))

print()
for row in sorted_list:
    print(row)
