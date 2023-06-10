# 트럭
# https://www.acmicpc.net/problem/13335

from collections import deque
import sys
f = sys.stdin.readline

n, w, L = map(int, f().split())
trucks = deque(list(map(int, f().split())))

# 다리 생성
bridge = deque([0]*w)
time = 0

# 다리에
while (bridge):
    # 1초가 지나면 다리 맨 왼쪽을 pop
    time += 1
    bridge.popleft()

    # 트럭이 남아있으면
    if trucks:
        # 다리 위의 하중을 계산한 후
        # 이 다음 트럭이 들어가지 못하면 0을 append
        if (sum(bridge)+trucks[0] > L):
            bridge.append(0)
        # 들어갈 수 있으면 트럭리스트에서 pop해서 다리에 append
        else:
            bridge.append(trucks.popleft())

print(time)
