t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    AB = a*b
    AC = a*c
    BC = b*c
    if AB < 0 or AC < 0 or BC < 0:
        print("YES")
    else:
        print("NO")
    t -= 1
