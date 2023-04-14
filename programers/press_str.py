# 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    n = len(s)

    # 문자열 길이 최솟값을 찾아야하므로, 최댓값인 처음 문자열 길이로 초기화
    answer = n

    # 반 이상 넘어가면 어차피 압축이 안되므로 반까지만
    for step in range(1, n//2 + 1):
        press = ''
        prev = s[:step]
        num = 1

        # prev이후부터 step만큼 옮겨가며 prev와 비교
        for i in range(step, n, step):
            now = s[i:i+step]
            if prev == now:
                num += 1
            else:
                # 숫자가 1 이상이면 숫자 포함해서, 아니면 이전 꺼만
                press += str(num)+prev if num > 1 else prev
                prev = now
                num = 1
        # step보다 작은 크기로 남은 문자열은 그대로 붙여준다
        press += str(num)+prev if num > 1 else prev
        answer = min(answer, len(press))

    return answer
