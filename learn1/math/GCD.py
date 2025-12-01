def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

t = int(input())

while t > 0:
    a, b = map(int, input().split())
    gcd_value = gcd(a, b) 
    
    print(gcd_value)
    t -= 1
