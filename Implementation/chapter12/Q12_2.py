# '현재 괜찮은 상태?' 를 구현하면 됌
# 설치 후 체크, 제거 후 체크.
# 안 괜찮으면 되돌리기

def is_ok(result):
    for a in result:
        x, y, bo = a
        if not bo: # 기둥 이면
            # 1.바닥에 있거나, 2.보의 한쪽 위에 있거나, 3.다른 기둥 위에 있거나
            if y==0 or [x, y, 1] in result or [x-1, y, 1] in result or [x, y-1, 0] in result:
                continue
            else:
                return False
        else: # 보 이면
            # 1.기둥 위에 있거나(한쪽이), 2.양쪽 끝이 보와 연결되거나
            if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    result=[]
    for build in build_frame:
        x, y, bo, oper = build
        if oper:
            result.append([x, y, bo])
            if not is_ok(result):
                result.pop()
        else:
            result.remove([x, y, bo])
            if not is_ok(result):
                result.append([x, y, bo])

    result.sort()
    return result