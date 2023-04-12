from collections import deque

# 리스트를 받아서 같은 문자를 압축해주는 함수
def cal_length(l):
    a = deque(l)
    result=[]
    left=a.popleft()
    count=1
    while True:
        if a:
            now_str = a.popleft()
        else:
            if count != 1:
                result.append(str(count))
            result.append(left)
            break
        if left==now_str:
            count+=1
        else:
            if count != 1:
                result.append(str(count))
            result.append(left)
            left=now_str
            count=1
    make_string=''.join(result)
    length=len(make_string)
    return length

def solution(s):
    if len(s)==1:
        return 1
    slicing_list=[]
    min_l=1000
    # 1부터 압축 단위를 늘려가며 문자열을 추출한다.
    # 문자열 길이의 반이 최대 압축 단위이므로 len(s)//2 +1 로 범위를 축소시킬 수 있다.
    for i in range(1,len(s)):
        slicing_list=[]
        for j in range(0,len(s),i):
            slicing_list.append(s[j:j+i])
        length = cal_length(slicing_list)
        min_l = min(min_l, length)
    answer=min_l
    return answer

data = "a"
print(solution(data))