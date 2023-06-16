# 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
durabilities = deque(list(map(int, input().split())))
robots = deque([False]*n)

def add_robot():
    if durabilities[0]>0:
        robots[0] = True
        durabilities[0]-=1
    
def drop_robot():
    robots[n-1] = False

def rotate_belt():
    durabilities.rotate(1)
    robots.rotate(1)
    

def move_robots():
    for i in range(n-2, -1, -1):
        # 현재 칸에 로봇이 있으면
        if robots[i]:
            # 다음 칸의 내구도가 0이 아니고 다음 칸에 로봇이 없으면
            if durabilities[i+1]>0 and not robots[i+1]:
                # 이동하고 내구도 -1
                robots[i] = False
                robots[i+1] = True
                durabilities[i+1] -=1
                

def check_durabilities():
    result = 0
    for durability in durabilities:
        if durability<=0:
            result+=1
    return result

answer =0
while(True):
    answer+=1
    rotate_belt()
    drop_robot()
    move_robots()
    drop_robot()
    add_robot()
    if check_durabilities()>=k:
        break
print(answer)
