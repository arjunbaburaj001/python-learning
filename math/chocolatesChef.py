t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    print(int((5 * x + 10 * y) / z))
    t -= 1
    