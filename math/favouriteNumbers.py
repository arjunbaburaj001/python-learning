t = int(input())

while t > 0:
    a = int(input())
    if a % 9 == 0 and a % 2. == 1:
        print("Bob")
    elif a % 7 == 0 and a % 2 == 0:
        print("Alice")
    else:
        print("Charlie")
    t -= 1
