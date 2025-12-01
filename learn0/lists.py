#Lists are also an ordered sequence, Lists are pretty similar to tuples
#Below is a normal list

L = [1,2,3,4,5]

#KEY DIFFERENCES COMPARED TO LISTS AND TUPLES

# - Lists are mutable (meaning you can change a value, or even modify the list itself)
#In this case the list is modified by extending the list values

L = List1

List1.extend([6,7])

# - Lists can not also extend but append as well. Appending adds whatever you put into the brackets become 1 whole value.
#Rather than extending which adds as many values depending on how many you put

List1.append([8,9])

# - Lists are mutable (meaning you can change a vlue, or even modify the list itself)
#In this case the list had a value changed in the index/list

List1 = [1,2,3,4,5]

List1[0] = "one"
#OR
del(List1[4])

#OTHER STUFF WITH LISTS

# - You can convert a string into a list using .split() similarly with tuples

VIEW Tuples.py

# - You can clone lists or duplicate them by using a colon (Keep in mind if you change 1st list, 2nd list will not change as it remains a copy of the origninal)

List2 = List1[:]

# - You can get much info by using the help command with either tuples, lists, or literally antyhing by doing help()