# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

# 구현할 때 생각을 많이 해야하는 문제이다
# (aaaao 에서 zzzzo)가 안되는 이유는 aaaap도 포함이 되어버린다
# 그래서 문자열을 뒤집은 리스트도 필요함

from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def solution(words, queries):
    # 리스트 생성
    data_div_len=[[] for _ in range(10001)]
    data_div_len_rev = [[] for _ in range(10001)]
    for w in words:
        data_div_len[len(w)].append(w)
        data_div_len_rev[len(w)].append(w[::-1])
        
    # 이진 탐색 위한 리스트 정렬
    for i in range(10001):
        data_div_len[i].sort()
        data_div_len_rev[i].sort()

    result=[]
    for q in queries:
        if q[0]=='?':
            rev = q[::-1]
            left_value = rev.replace('?', 'a')
            right_value = rev.replace('?', 'z')
            array = data_div_len_rev[len(rev)]
        else:
            left_value = q.replace('?', 'a')
            right_value = q.replace('?', 'z')
            array = data_div_len[len(q)]
        result.append(count_by_range(left_value, right_value, array))
            
    return result


def count_by_range(left_value, right_value, array):
    if array==None:
        return 0
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index-left_index

print(solution(words, queries))