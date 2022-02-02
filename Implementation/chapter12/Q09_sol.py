

def solution(s):
    answer=len(s)
    for step in range(1, len(s)//+1):
        prev = s[0:step]
        count=1
        compressed=""
        for i in range(step, len(s), step):
            if prev==s[i:i+step]:
                count+=1
            else:
                compressed+= str(count)+prev if count>1 else prev
                prev = s[i:i+step]
                count=1
        compressed+= str(count)+prev if count>1 else prev
        answer = min(answer, len(compressed))
    return answer
