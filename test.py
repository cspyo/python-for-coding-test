from collections import deque

q = deque([])
q.append([7, 2])
q.append([3, 2])
print(q)
print(q[0][1])
print(q[0][1] == 2)
print(sum(q[0]))
