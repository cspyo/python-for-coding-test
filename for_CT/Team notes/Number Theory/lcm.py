x = 24
y = 32

''' 최대공약수(a,b의 가장 큰 공약수) '''
def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

''' 최소공배수 '''
def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(x, y))
