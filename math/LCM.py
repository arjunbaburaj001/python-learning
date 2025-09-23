def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

t = int(input())

while t > 0:
    a, b = map(int, input().split())
    gcd_value = gcd(a, b)
    lcm_value = (a * b) // gcd_value  
    
    print(lcm_value)
    t -= 1
