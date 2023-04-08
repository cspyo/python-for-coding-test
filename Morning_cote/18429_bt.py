# 근손실
# https://www.acmicpc.net/problem/18429
# 백트래킹

from itertools import permutations
import sys
f = sys.stdin.readline

n, k = map(int, f().rstrip().split())
kit = list(map(int, f().rstrip().split()))

MIN_WEIGHT = 500


def dfs(days, weight):
    global count
    if (days == n):
        count += 1
        return
    for i in range(n):
        weight_after = weight+kit[i]-k
        if (used_kit[i] or weight_after < MIN_WEIGHT):
            continue
        used_kit[i] = True
        dfs(days+1, weight_after)
        used_kit[i] = False


used_kit = [False]*n
count = 0

dfs(0, MIN_WEIGHT)
print(count)
