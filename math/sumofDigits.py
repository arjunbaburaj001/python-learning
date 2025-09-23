t = int(input())
for _ in range(t):
    n = int(input())
    sum = 0
    while n != 0:
        d = n % 10
        sum += d
        n //= 10
    print(sum)

'''
Steps:
Initialize a variable to store the sum of digits (lets call it sum). Use a loop to repeatedly extract the last digit of N
using the modulus operator (% 10), add this digit to sum, and then remove the last digit by dividing N by 10 (N = N/10).
Continue this process until N becomes 0.
'''