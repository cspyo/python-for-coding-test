# 보물찾기
import heapq as hq
INF=int(1e9)

def dijkstra(graph, n):
    d=[INF]*(n+1)
    h=[]
    hq.heappush(h, (1,0))
    d[1]=0
    while h:
        v, c = hq.heappop(h)
        for g_v, g_c in graph[v]:
            if (g_c+c)<d[g_v]:
                d[g_v] = g_c+c
                hq.heappush(h, (g_v, d[g_v]))
    return d

def main():
    n, m = map(int, input().split())
    graph=[[]*(n+1) for _ in range(n+1)]
    value=[0 for _ in range(n+1)]
    for _ in range(n-1):
        a, b, d = map(int, input().split())
        graph[a].append((b,d))
    for _ in range(m):
        a, v = map(int, input().split())
        value[a]=v
    
    di=dijkstra(graph, n)
    
    result_v=0
    result_c=-INF
    for i in range(2, n+1):
        x = value[i]-(di[i]*2)
        if result_c<x:
            result_c=x
            result_v=i
    print(result_v, result_c)

    
if __name__=="__main__":
    main()