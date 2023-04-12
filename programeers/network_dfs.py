# 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# dfs

def dfs(i, visited, computers, n):
    visited[i] = True
    for j in range(n):
        if computers[i][j] == 1:
            if not visited[j]:
                dfs(j, visited, computers, n)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers, n)
            answer += 1

    return answer
