# 팰린드롬?
# https://www.acmicpc.net/problem/10942

import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
m = int(input())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

def make_palindrome_dp():
    for i in range(n):
        for start in range(n-i):
            end = start+i
            
            if start == end: # 글자가 1개이면 무조건 팰린드롬
                dp[start][end] = 1
                continue
            
            if num_list[start]==num_list[end]: # 맨 앞과 맨 끝의 문자가 같을 때
                if start+1 == end: # 길이가 딱 2라면 팰린드롬 (1,1)
                    dp[start][end] = 1
                    continue
                
                if dp[start+1][end-1] == 1: # 가운데 문자열이 팰린드롬이면 팰린드롬
                    dp[start][end] = 1

make_palindrome_dp()

question = []
for _ in range(m):
    start, end = map(int, input().split())
    question.append([start, end])

for start, end in question:
    print(dp[start-1][end-1])
