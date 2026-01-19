# cook your dish here
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    third = 21 - (a + b)
    
    if 1 <= third <= 10:
        print(third)
    else:
        print(-1)