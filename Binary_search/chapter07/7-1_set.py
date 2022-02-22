import sys

f = sys.stdin.readline

n = int(f().rstrip())
all = set(map(int, f().rstrip().split()))
m = int(f().rstrip()) 

for r in list(map(int, f().rstrip().split())):
    if r in all:
        print("yes", end=' ')
    else:
        print("no", end=' ')