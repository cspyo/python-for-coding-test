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
        if build[3]:
            if build[2]==0:
                if check_gd(build[0], build[1], gd_list, bo_list):
                    gd_list.append((build[0],build[1]))
                    result.append([build[0], build[1], 0])
            else:
                if check_bo(build[0], build[1], gd_list, bo_list):
                    bo_list.append((build[0],build[1]))
                    result.append([build[0], build[1], 1])
        else:
            if build[2]==0:
                gd_list.remove((build[0],build[1])) # 일단 삭제해
                # 기둥 하나를 삭제하면 1.아래 있는 기둥, 2.위에 있는 보 두개
                if check_gd(build[0], build[1]+1, gd_list, bo_list) and check_bo(build[0], build[1]+1, gd_list, bo_list) and check_bo(build[0]-1, build[1]+1, gd_list, bo_list):
                    result.remove([build[0], build[1], 0])
                else:
                    gd_list.append((build[0], build[1]))
            else:
                bo_list.remove((build[0], build[1]))
                # 보를 삭제하면 1.양쪽 위에 있는 기둥, 2.양쪽에 연결된 보
                if check_gd(build[0], build[1], gd_list, bo_list) and check_gd(build[0]+1, build[1], gd_list, bo_list) and check_bo(build[0]-1, build[1], gd_list, bo_list) and check_bo(build[0]+1, build[1], gd_list, bo_list):
                    result.remove([build[0], build[1], 1])
                else:
                    bo_list.append((build[0],build[1]))
    # print(gd_list)
    # print(bo_list)                
    # print(sorted(result))

    
    
    return sorted(result)

# n=5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],
# [5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n=5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],
[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

solution(n, build_frame)