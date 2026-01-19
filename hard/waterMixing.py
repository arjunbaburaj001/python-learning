# cook your dish here
t = int(input())

for _ in range(t):
    a, b, x, y = map(int, input().split())
    
    if b == a:
        print('YES')
    elif b > a:
        if (b - a) <= x:
            print('YES')
        else:
            print('NO')
    else:  # This means b < a
        if (a - b) <= y:
            print('YES')
        else:
            print('NO')