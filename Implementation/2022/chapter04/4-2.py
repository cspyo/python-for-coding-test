# 시각

n = int(input())

count=0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            h, m, s = map(str, (h, m, s))
            sum = h+m+s
            # if '3' in str(h)+str(m)+str(n):
            if sum.find('3')!=-1:
                count+=1 
            
print(count)

