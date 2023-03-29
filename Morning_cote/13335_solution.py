# 트럭
# https://www.acmicpc.net/problem/13335

from collections import deque
import sys
f = sys.stdin.readline

n, w, L = map(int, f().split())
trucks = deque(list(map(int, f().split())))

bridge = deque([0]*w)
time = 0
while (bridge):
    time += 1
    bridge.popleft()
    if trucks:
        if (sum(bridge)+trucks[0] > L):
            bridge.append(0)
        else:
            bridge.append(trucks.popleft())

print(time)
