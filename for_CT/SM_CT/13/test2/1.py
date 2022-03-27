# 선호도
import sys
from itertools import combinations
input = sys.stdin.readline

def main():
    n, m, k = map(int, input().split())
    sunho=[]
    menu=[i for i in range(m)]
    for _ in range(n):
        sunho.append(list(map(int, input().split())))
    
    people=0
    max_value=0
    for a in combinations(menu, m-k):
        for s in sunho:
            count=0
            for i in a:
                if s[i]>=5:
                    count+=1
            if count>=1:
                people+=1
        max_value=max(max_value, people)
        people=0

    print(max_value)
    
if __name__=="__main__":
    main()