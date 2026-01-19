# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    difficulties = list(map(int, input().split()))
    count = 0
    
    for difficulty in difficulties:
        if difficulty >= 1000:
            count += 1
    
    print(count)