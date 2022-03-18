# 자동완성
# 전체 문자열을 주고
# s 넣으면 sm, sleerk, soker 이런거 개수
# sm 넣으면 smtoen, smalf, smdskls 이거 개수

def main():
    n=int(input())
    data=[]
    for _ in range(n):
        data.append(input())
    t=int(input())
    inputing=[]
    for _ in range(t):
        inputing.append(input())
    
    result=[]
    for i in inputing:
        count=0
        for d in data:
            if d[:len(i)]==i:
                count+=1
        result.append(count)
    
    for r in result:
        print(r)

if __name__=="__main__":
    main()