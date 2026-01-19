# cook your dish here
t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    count = 0
    
    while n > x:
        x += 4
        count += 1
        
    print(count)