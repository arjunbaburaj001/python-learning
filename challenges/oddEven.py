def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1  
        else:
            odd_count += 1

    return even_count, odd_count  

n = int(input("How many numbers? "))
a = [0] * n  

for counter in range(n):
    a[counter] = int(input("Enter a number: "))

even_count, odd_count = count_even_odd(a)

print("Odd numbers:", odd_count)
print("Even numbers:", even_count)
