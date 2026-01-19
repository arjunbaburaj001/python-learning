# cook your dish here
t = int(input())

for _ in range(t):
    a, b, x, y = map(int, input().split())
    ab = a * b
    xy = x * y
    
    if xy >= ab:
        print("YES")
    else:
        print("NO")