#A great way to make a Python for loop that changes or creates a list easier is by turning it into one line of code.

old_list = [1, 2, 3, 4, 5]
new_list = []
for i in old_list:
    if i % 2 == 1:
        new_list.append(i * 2)
print(new_list)

#This transforms an old list by making it if a number is odd, we add the number times 2 (*2) into the array
#This makes a new list where all the code from the old list as well as the added on functions applied to the old list is tranformed into one line of code which is the new list.