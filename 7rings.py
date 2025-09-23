t = int(input())

while t > 0:
    n, x = map(int, input().split())
    total = n * x
    if len(str(total)) == 5:
        print("YES")
    else:
        print("NO")
    t -= 1
