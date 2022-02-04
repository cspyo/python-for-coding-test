li = [[i*3+j for j in range(3)] for i in range(3)]
li = list(zip(*li[::-1]))
for item in li:
	print(*item)




# 결과
