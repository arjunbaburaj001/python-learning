listExample = [1, 2, 3, 4, 5]

for i in range(len(listExample)):
    print(listExample[i], end=" ")
print()

for element in listExample:
    print(element, end=" ")
print()

#This makes a regular for loop to iterate (or go through 1 by 1) all the elements of the list




iterators = iter(listExample)

print(next(iterators)) #1
print(next(iterators)) #2

#Allows you to traverse a container (similarly to iterating but checking every item from start to finish)