#Tuples are an ordered sequence, they are also written as comma_separated elements within parentheses
#Below is an example of a Tuple
Ratings = (10,9,5,4,3,6,2,8,10,1)

tuple1 = ("test",10,2.67)

#You can access the value in the tuple by using a bracket with the index number (You can also use a negative index as well)

tuple1[0] #Result - "test"
tuple1[1] #Result - 10
tuple1[2] #Result - 2.67

#You can also combine tuples also known as concatenating shown below

tuple2 = (2,14.7,"ball")
tuple3 = tuple2 + tuple1 #Result - ("test",10,2.67,2,14.7,"ball")

#You can also slice tupes by using a colon in between the numbers assigned to slice

tuple3[0:3]
tuple3[3:5]

#You can determine the length of a tuple using "len"

len(("test",10,2.67)) #Result - 5

#Tuples are immutable, in other words if you want to change a value in one of the index values, it is not possible as they are immutable

Ratings[3] = 4 #Result - ERROR

#However you can make another tuple instead, such as sorting as shown below

RatingsSorted = sorted(Ratings)

#Tuples can also contain other tuples inside one another, this is known as nesting

Nesting = (1,2,("test",3),4,5)