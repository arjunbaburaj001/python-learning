#RANGE
#The range funtion lists all values in the following integer given

range(4) #Result = 0,1,2,3
range(10,15) #Result = 10,11,12,13,14


#FOR LOOPS

Squares = ["red", "yellow", "green", "blue", "purple"]

for i in range(0,5):
    Squares[0] = "red"

#This changed the blue color into red 5 times


#WHILE LOOPS
 
squaresList = ["orange", "orange", "yellow", "orange"]
i=0

squaresList2 = []

while(squaresList[i]=='orange'):
    squaresList2.append(squaresList[i])
    i=i+1
    print("orange, TRUE")
