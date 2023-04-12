# 문자열 압축

def solution(s):
    # answer이 가장 짧은 길이의 문자열이 될테니
    # 최댓값인 현재 문자열의 길이로 초기화
    answer=len(s)
    for step in range(1, len(s)//+1):
        prev = s[0:step]
        count=1
        compressed=""
        for i in range(step, len(s), step):
            if prev==s[i:i+step]:
                count+=1
            else:
                # 중복문자가 없으면 1은 생략해서 문자열을 만든다.
                compressed+= str(count)+prev if count>1 else prev
                prev = s[i:i+step]
                count=1
        # 마지막 문자는 비교할 대상이 없이 바로 for문을 빠져나오기에 한번 더 압축을 해줘야한다.
        compressed+= str(count)+prev if count>1 else prev
        answer = min(answer, len(compressed))
    return answer
