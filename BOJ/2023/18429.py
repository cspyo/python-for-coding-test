# 근손실
# https://www.acmicpc.net/problem/18429
# 브루트포스

from itertools import permutations
import sys
f = sys.stdin.readline

n, k = map(int, f().rstrip().split())
kit = list(map(int, f().rstrip().split()))

all_selections = list(permutations(kit, n))


def check(selection):
    now = 500
    for i in selection:
        now += i-k
        if (now < 500):
            return False
    return True


result = 0
for selection in all_selections:
    if (check(selection)):
        result += 1

print(result)
