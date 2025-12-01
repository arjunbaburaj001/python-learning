class Character: #Creates a class

    def __init__(self, name): #Initalizes method using self
        self.name = name

    def say_hello(self): #An example of a object
        print("Hello, my name is ", self.name)

object = Character("Arjun") #Calls the object for 9 and 10 python lines
object.say_hello()


'''Classes are basically blueprints or something that defines
a structure holdiing attributes and methods. The '''