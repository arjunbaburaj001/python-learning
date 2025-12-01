import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    gcd = math.gcd(n, m)
    num_squares = (n * m) // (gcd * gcd)
    print(num_squares)