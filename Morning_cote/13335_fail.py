# 트럭
# https://www.acmicpc.net/problem/13335

from collections import deque
import sys
f = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(list(map(int, f().rstrip().split())))

INF = 1e9
trucks.append(INF)


def sum_weight(q):
    sum = 0
    for item in q:
        sum += q[0][0]
    return sum


on_the_bridge = deque([])
on_the_bridge.append([0, 0])
time = 0
while True:
    if (on_the_bridge[0][1] == 0):
        on_the_bridge.popleft()
    if (sum_weight(on_the_bridge)+trucks[0] <= L):
        truck = trucks.popleft()
        on_the_bridge.append([truck, w])
    time += 1
    for i in range(len(on_the_bridge)):
        on_the_bridge[i][1] -= 1
    if (not on_the_bridge):
        break

print(time)
