# 숫자 카드 게임


# # 처음 풀었을때
# cards=[]
# n,m = map(int,input().split())
# for _ in range(n):
#   card = list(map(int, input().split()))
#   card.sort()
#   cards.append(card)

# max = cards[0][0]

# for i in range(n):
#   if cards[i][0] >= max:
#     max = cards[i][0]

# print(max)


#두번째
min_list=[]
n,m = map(int,input().split())
for _ in range(n):
  card = list(map(int, input().split()))
  min_list.append(min(card))

print(max(min_list))

#답안

result=0
n,m = map(int,input().split())
for _ in range(n):
  card = list(map(int, input().split()))
  min_value = min(card)
  result = max(result, min_value)

print(result)