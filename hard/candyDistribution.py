t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    equal_candies = n // m
    
    if n % m == 0:
        if equal_candies % 2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print("NO")