# 자물쇠와 열쇠
# https://school.programmers.co.kr/learn/courses/30/lessons/60059


def rotate_key_90_degree(key):
    n = len(key)
    m = len(key[0])

    new_key = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_key[j][n-i-1] = key[i][j]
    return new_key


def check(lock_tmp, n):
    for i in range(n):
        for j in range(n):
            if lock_tmp[i][j] == 0 or lock_tmp[i][j] == 2:
                return False
    return True


def sliding(key, lock, m, n):
    for a in range(-m+1, n):
        for b in range(-m+1, n):
            lock_tmp = [item[:] for item in lock]
            for i in range(m):
                for j in range(m):
                    if 0 <= i+a < n and 0 <= j+b < n:
                        lock_tmp[i+a][j+b] += key[i][j]
            if (check(lock_tmp, n)):
                return True
    return False


def solution(key, lock):
    answer = sliding(key, lock, len(key), len(lock))
    for _ in range(3):
        key = rotate_key_90_degree(key)

        if sliding(key, lock, len(key), len(lock)):
            return True

    return answer
