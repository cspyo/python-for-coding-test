# BOJ 11779 최소비용 구하기 2
# https://www.acmicpc.net/problem/11779

import sys
import heapq as hq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())
distance = [INF] * (n+1)
parents = [0 for _ in range(n+1)]

def dijkstra(start):
    q = []
    distance[start] = 0
    hq.heappush(q, (distance[start], start))
    while q:
        d, now = hq.heappop(q)
        if (distance[now] < d):
            continue
        
        for next_node, node_distance in graph[now]:
            cost = d + node_distance
            if (cost < distance[next_node]):
                parents[next_node] = now
                distance[next_node] = cost
                hq.heappush(q, (cost, next_node))
    
def printPath():
    global parents
    global end
    path = []
    while (end != 0):
        path.append(end)
        end = parents[end]
    
    print(len(path))
    print(*path[::-1]) 
        
dijkstra(start)
print(distance[end])
printPath()
    


# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5