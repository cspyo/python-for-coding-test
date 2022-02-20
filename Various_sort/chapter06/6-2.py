# 성적이 낮은 순서로 학생 출력하기
import sys
f = sys.stdin.readline

n = int(f())
array=[]
for _ in range(n):
    name, score = f().split()
    array.append((name, int(score)))

array.sort(key=lambda x: x[1])

for a,b in array:
    print(a, end=' ')

