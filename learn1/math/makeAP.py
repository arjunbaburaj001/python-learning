t = int(input())

while t > 0:
    a, c = map(int, input().split())
    print((a+c)//2 if a%2 == c%2 else -1)
    t -= 1
