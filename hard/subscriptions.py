# cook your dish here
t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    
    subscriptions = (n + 5) // 6
    total_cost = subscriptions * x
    print(total_cost)