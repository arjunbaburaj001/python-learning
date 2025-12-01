Name = "Michael Jackson"

#Grabs the letter from the assigned number from string (Works with negative indexes as well)
Name[0] #Result = M
Name[12] #Result = s
Name[4] #Result = a

#Treats the string as a sequence, takes all values in between the assigned numbers
Name[0:4]
Name[8:12]

#Can multiply the amount of times the string is repeated
3* "Michael Jackson"

#Using /{letter} can have a big effect such as adding a new line
print("Michael Jackson /n is the best") #Result = Michael Jackson (New Line) is the best
print("Michael Jackson /t is the best") #Result = Michael Jackson (Tab) is the best

#Using double / puts an actual / into the string (Only 1 of them, not 2, you could also use letter r instead of double /)
print("Michael Jackson // is the best")
print(r"Michael Jackson is the best")