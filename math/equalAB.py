for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    while a < b:
        a *= 2
    print('yes' if a == b else 'no')

'''if a is gretaer than b then flip the ordered pair to (b, a) rather than (a, b).
While b is greater than b we can multiply by 2 until both values become equal to each
other where we then print yes or no depending on the 2 values, but in this case, yes'''