# 모험가 길드
from collections import deque
import sys

f = sys.stdin.readline

n = int(input())
people = list(map(int, f().rstrip().split()))

sorted_people = deque(sorted(people))

result = 0
end_of_group = False
while (len(sorted_people) != 0):
    person = sorted_people[0]
    for _ in range(person):
        if (len(sorted_people) == 0):
            end_of_group = True
            break
        else:
            sorted_people.popleft()
    if (not end_of_group):
        result += 1

print(result)
