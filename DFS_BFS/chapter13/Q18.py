# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

def balance(s):
    count=0
    for i in range(len(s)):
        if s[i]=='(':
            count+=1
        else:
            count-=1
        if count==0:
            return i

def correct(s):
    a=[]
    for i in s:
        a.append(i)
        if "".join(a[-2:])=="()":
            a[-2:]=[]
    if a:
        return False
    else:
        return True

def dfs(s):
    answer=''
    if s=='':
        return answer
    index = balance(s)
    u=s[:index+1]
    v=s[index+1:]
    if correct(u):
       answer = u + dfs(v)
    else:
        answer += "("
        answer+=dfs(v)
        answer+=")"
        u=u[1:-1]
        for a in u:
            if a=="(":
                answer+=")"
            else:
                answer+="("
    return answer

def solution(p):
    if correct(p):
        return p
    else:
        return dfs(p)


p="()))((()"
print(solution(p))