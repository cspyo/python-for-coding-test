# 삼분값
# 처음에 두개 숫자
# 3개씩 n번 추가
# 추가할때마다 삼분값 제출
# 삼분값 : 값 기준으로 나눠진 수열의 길이가 모두 같은거

# 이건 속도 빠르게 안되나
# 정렬된 배열에 숫자를 추가할때 빠르게 추가할 수 있나 고민
# 투 포인터 사용하면 되려나


def main():
    a,b=map(int, input().split())
    n=int(input())
    data=[]
    data.append(a)
    data.append(b)
    one=1
    two=3
    result=[]
    for _ in range(n):
        for d in list(map(int, input().split())):
            data.append(d)
        data.sort()
        result.append((data[one], data[two]))
        one+=1
        two+=2
    for r in result:
        print(r[0], r[1])
    
    

if __name__=="__main__":
    main()