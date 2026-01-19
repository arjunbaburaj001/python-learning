# cook your dish here
t = int(input())

for _ in range(t):
    n, k, m = map(int, input().split())
    # n = number of candies
    # k = number of pockets
    # m = maximum of candies in each pocket
    km = k * m
    if n < km:
        print(1)
    else:
        if n % km == 0:
            print(n // km)
        else:
            print((n // km) + 1)