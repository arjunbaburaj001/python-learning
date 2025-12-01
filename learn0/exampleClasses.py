class Person:
    def __init__(self, name, age):
        """
        Creates a class with attributes name, age and adds self
        which is the object and not just a normal variable but an
        attribute you can apply to using '.'
        """
        self.name = name
        self.age = age

    def display_info(self):
        """Display the person's name and age."""
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing attributes and calling methods
person1.display_info()  # Output: Name: Alice, Age: 30
person2.display_info()  # Output: Name: Bob, Age: 25

# Modifying attributes
person1.age = 31
print(f"{person1.name} is now {person1.age} years old.")  # Output: Alice is now 31 years old.
