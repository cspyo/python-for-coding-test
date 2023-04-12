## 개똥망 테스트케이스는 되는데 채점하면 엉망임

def check_gd(x, y, gd_list, bo_list):
    if (x,y) in bo_list or (x-1,y) in bo_list or (x,y-1) in gd_list or y==0:
        return True
    return False

def check_bo(x, y, gd_list, bo_list):
    if ((x-1,y) in bo_list and (x+1,y) in bo_list) or (x,y-1) in gd_list or (x+1,y-1) in gd_list:
        return True
    return False

def solution(n, build_frame):
    gd_list=[]
    bo_list=[]
    result=[]
    for build in build_frame:
        x, y, what, operation = build
        if operation: # 설치
            if what==0: # 기둥
                if check_gd(x, y, gd_list, bo_list):
                    gd_list.append((x,y))
                    result.append([x, y, 0])
            else: # 보
                if check_bo(x, y, gd_list, bo_list):
                    bo_list.append((x,y))
                    result.append([x, y, 1])
        else: # 삭제
            if what==0: # 기둥
                gd_list.remove((x,y)) # 일단 삭제해
                # 기둥 하나를 삭제하면 그 기둥과 관련있는 모든 것 ---> 여기도 잘못됨
                # 여기 부분이 잘못됨
                if check_gd(x, y-1, gd_list, bo_list) and check_gd(x, y+1, gd_list, bo_list) and check_bo(x-1, y, gd_list, bo_list) and check_bo(x, y, gd_list, bo_list) and check_bo(x-1, y+1, gd_list, bo_list) and check_bo(x, y+1, gd_list, bo_list):
                    result.remove([x, y, 0])
                else:
                    gd_list.append((x, y))
            else: # 보
                bo_list.remove((x, y))
                # 보를 삭제하면 그 보와 관련된 모든 것 ---> 이 생각이 잘못된듯
                # 여기 부분이 잘못됨
                if check_gd(x, y, gd_list, bo_list) and check_gd(x, y-1, gd_list, bo_list)  and check_gd(x+1, y, gd_list, bo_list) and check_gd(x+1, y-1, gd_list, bo_list) and check_bo(x-1, y, gd_list, bo_list) and check_bo(x+1, y, gd_list, bo_list):
                    result.remove([x, y, 1])
                else:
                    bo_list.append((x,y))
    print(gd_list)
    print(bo_list)                
    print(sorted(result))

    
    
    return sorted(result)

# n=5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],
# [5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n=5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],
[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

solution(n, build_frame)