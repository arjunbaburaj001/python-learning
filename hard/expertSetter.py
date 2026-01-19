# cook your dish here
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    if (2*y) >= x:
        print("YES")
    else:
        print("NO")