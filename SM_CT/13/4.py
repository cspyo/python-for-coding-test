# 식단 짜기
# 이건 그냥 dfs 문제인듯 백트래킹
# dfs로도 해보는게 좋을듯 메뉴가 십만이였나...
# 칼로리 2000 이상 2500이하의 식단짜기
# 서로 다른 3개, 순서 고려, 중복 x
# 

from itertools import combinations

def main():
    n = int(input())
    data=list(map(int, input().split()))

    count=0
    for comb in list(combinations(data, 3)):
        if 2000<=sum(comb)<=2500:
            count+=1

    print(count)

if __name__=="__main__":
    main()