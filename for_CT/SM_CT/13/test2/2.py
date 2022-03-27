#  만족도 조사
# union-find 해야할듯
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def main():
    n, m, k = map(int, input().split())
    manjok=[0] * (n+1)
    for _ in range(m):
        i, s = map(int, input().split())
        manjok[i]=s
    
    # 친구관계
    parent=[0] * (n+1)
    for i in range(1, n+1):
        parent[i]=i

    for _ in range(k):
        a, b = map(int, input().split())
        union_parent(parent, a, b)
    
    f=[[] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==parent[j]:
                f[i].append(j)
    
    manjok_set=[0] * (n+1)
    for i in range(1, len(f)):
        if not f[i]:
            continue
        result=0
        count=0
        for a in f[i]:
            if manjok[a]!=0:
                result+=manjok[a]
                count+=1
        if result!=0:
            manjok_set[i]=(result//count)
    
    for i in range(1, n+1):
        if manjok[i]==0:
            manjok[i]=manjok_set[parent[i]]
    
    result=0
    count=0
    for m in manjok:
        if m!=0:
            result+=m
            count+=1

    x = result/count
    x=int(x*100)
    x=x/100
    
    print("{:.2f}".format(x))


if __name__=="__main__":
    main()