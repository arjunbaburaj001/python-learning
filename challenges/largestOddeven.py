def largest_odd_even_count(numbers):
    even_count = None
    odd_count = None

    for n in numbers:
        if n % 2 == 0:
            if even_count is None or n > even_count:
                even_count = n
        else:
            if odd_count is None or n > odd_count:
                odd_count = n
    
    return even_count, odd_count

n = int(input())
a = [0] * n 

for counter in range(n):
    a[counter] = int(input())

even_count, odd_count = largest_odd_even_count(a)

print(even_count)
print(odd_count)