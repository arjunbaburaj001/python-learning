t = int(input())

while t > 0:
    x, y = map(int, input().split())
    if x >= y:
        print(y)
    else:
        print(x + (y-x) * 2)
        
    t -= 1
