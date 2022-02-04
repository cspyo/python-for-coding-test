def rotate_key(a):
    n = len(a)
    m = len(a[0])
    res = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][n-1-i] = a[i][j]
    return res

def is_lock(pad_lock):
    lock_len = len(pad_lock) // 3
    for i in range(lock_len, lock_len*2):
        for j in range(lock_len, lock_len*2):
            if pad_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(key)
    m = len(lock)
    pad_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            pad_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_key(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        pad_lock[x+i][y+i] += lock[i][j]
                if is_lock(pad_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        pad_lock[x+i][y+i] -= lock[i][j]
    return False