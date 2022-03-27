# 복호화
# a X 글자 + b = ???
# alpha[???%26] 암호화
# 복호화 하는 알고리즘

def main():
    a,b=map(int, input().split())
    t=input()
    alpha=[chr(i) for i in range(97, 97+26)]
    result=[]
    for c in t:
        x = ord(c)%97
        if x==b:
            result.append(alpha[0])
            continue
        x=x+26-b
        # 여기를 고쳐야할듯
        # if x%a!=0:
        #     x+=26
        while x%a==0:
            x+=26
        # 이렇게 고치면 완벽할듯
        x=x//a
        result.append(alpha[x])
    
    print("".join(result))

if __name__=="__main__":
    main()

