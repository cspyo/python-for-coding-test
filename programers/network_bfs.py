# 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# bfs

from collections import deque


def bfs(i, visited, computers, n):
    q = deque([i])
    while q:
        now = q.popleft()
        visited[now] = True
        for j in range(n):
            if computers[now][j] == 1 and not visited[j]:
                q.append(j)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers, n)
            answer += 1
    return answer
