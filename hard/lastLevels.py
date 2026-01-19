# cook your dish here
t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    # x = levels remaining
    # y = minutes to complete
    # z = break
    total_time = x * y
    
    if x % 3 == 0:
        breaks = (x // 3) - 1
    else:
        breaks = x // 3
    
    total_time += breaks * z
    print(total_time)
        
        