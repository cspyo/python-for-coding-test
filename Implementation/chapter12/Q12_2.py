# 답안 코드를 바탕으로 내가 짠 코드 수정해보기
# 처음 문제를 보고 생각한 '현재 괜찮은 상태?' 를 구현하면 됌
# 설치 후 체크, 제거 후 체크.
# 안 괜찮으면 되돌리기

def is_ok(result):
    for a in result:
        x, y, stuff = a
        if stuff==0:
            if y==0 or [x, y, 1] in result or [x-1, y, 1] in result or [x, y-1, 0] in result:
                continue
            else:
                return False
        else:
            if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    result=[]
    for build in build_frame:
        x, y, stuff, oper = build
        if oper:
            result.append([x, y, stuff])
            if not is_ok(result):
                result.pop()
        else:
            result.remove([x, y, stuff])
            if not is_ok(result):
                result.append([x, y, stuff])

    result.sort()
    return result