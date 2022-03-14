# 이거 나중에 확인

import sys
input = sys.stdin.readline

N = int(input())
nums = tuple(map(int, input().strip().split()))
ops = list(map(int, input().strip().split()))

res_max = -1e10
res_min = 1e10

operations = [lambda a,b: a+b, lambda a,b: a-b, lambda a,b: a*b, lambda a,b: int(a/b)]

def dfs(val, idx):
    global res_min, res_max
    if idx == len(nums):
        res_min = min(res_min, val)
        res_max = max(res_max, val)
        return

    for op in range(4):
        if ops[op] == 0:
            continue
        ops[op] -= 1
        dfs(operations[op](val, nums[idx]), idx+1)
        ops[op] += 1

dfs(nums[0], 1)
print(res_max)
print(res_min)