def is_unlock(m,n,tmp):
    for i in range(n):
        for j in range(n):
            if tmp[i+m-1][j+m-1]==0:
                return False
    return True

def key_rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def solution(key, lock):
    m = len(key)
    n = len(lock)
    pad=n+2*(m-1)
    zero_padding = [[0]* pad for _ in range(pad)]
    for i in range(n):
        for j in range(n):
            zero_padding[i+m-1][j+m-1] = lock[i][j]
    
    # 2차원 리스트의 깊은 복사
    tmp = [item[:] for item in zero_padding] 

    # 4 방향에 대해 확인
    for _ in range(4):
        for k in range(pad-m+1):
            for y in range(pad-m+1):
                for i in range(k,k+m):
                    for j in range(y,y+m):
                        if zero_padding[i][j]==0 and key[i-k][j-y]==1:
                            tmp[i][j]=1
                        elif zero_padding[i][j]==1 and key[i-k][j-y]==1:
                            tmp[i][j]=0
                if is_unlock(m,n,tmp):
                    return True
                tmp = [item[:] for item in zero_padding]
        key = key_rotated(key)
    return False
                
        
        
    
key = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
lock = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
print(solution(key, lock))



## deepcopy 랑 슬라이싱하는거
## 깊은 복사 얕은 복사 블로그에 정리하기