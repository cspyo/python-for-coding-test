# 볼링공 고르기

n,m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트 생성
arr=[0]*10

for x in data:
  #각 무게에 해당하는 볼링공 개수 카운트
  arr[x-1]+=1

result=0
# 무게가 적은거부터 A가 선택한다고 가정
for i in range(m):
  n -= arr[i] # A가 선택한 무게의 볼링공 개수를 전체 개수에서 제외
  result += arr[i]*n # B가 선택하는 경우의 수와 곱하기

print(result)