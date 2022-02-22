# 카드 정렬하기
# BOJ 1715

# 내 생각에는 카드뭉치들을 정렬하고 앞에서부터 차례대로 더해나가는게 최소일거 같음
# 왜 그런지는 좀 더 생각해봐야할듯

# 차례로 더해나가는게 아니라 (항상 카드 뭉치 중에 가장 작은 두 개)를 더해나갈 때
# 가장 최솟값이네
# 그리디네

# 해답을 봐버려서 우선순위 큐를 사용해서 항상 작은 두개를 골라내는거까지 알아버림
# 구현은 성공~

import heapq
import sys
f = sys.stdin.readline

n = int(f())
data=[]
for _ in range(n):
    heapq.heappush(data, int(f()))

result=0
while len(data)>1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    prev=a+b
    result=result+prev
    heapq.heappush(data, prev)

print(result)