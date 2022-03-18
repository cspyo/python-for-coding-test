x = 24
y = 32

''' 최대공약수 '''
def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

print(gcd(x, y))
