
# 괄호 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058#

def is_balanced(arr):
    return arr.count("(") == arr.count(")")


def is_right(arr):
    is_right = 0
    for item in arr:
        if (item == "("):
            is_right += 1
        else:
            is_right -= 1
        if (is_right < 0):
            return False
    return True


def recursion(arr):
    if not arr or is_right(arr):
        return arr

    # 문자열 분리
    for i in range(1, len(arr)+1):
        u = arr[:i]
        if (is_balanced(u)):
            v = arr[i:]
            if (is_right(u)):
                return u + recursion(v)
            else:
                new_str = "("
                new_str += recursion(v)
                new_str += ")"

                for item in u[1:-1]:
                    if item == '':
                        continue
                    if (item == "("):
                        new_str += ")"
                    else:
                        new_str += "("
                return new_str


def solution(p):
    answer = recursion(p)
    return answer
