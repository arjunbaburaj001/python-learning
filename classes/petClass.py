class Pet:
    def __init__(self, name, species, hunger_level=5):
        self.name = name
        self.species = species
        self.hunger_level = hunger_level

    def feed(self):
        self.hunger_level = max(0, self.hunger_level - 1)  # Prevents going below 0

    def play(self):
        self.hunger_level = min(10, self.hunger_level + 2)  # Prevents going above 10

    def pet_status(self):
        return f"{self.name}, {self.species}, Hunger Level: {self.hunger_level}"

# Create pet objects
dog = Pet("Milo", "Cocker Spaniel", 5)
cat = Pet("Luna", "Maine Coon", 5)

# Check initial status
print(cat.pet_status())  # Output: Luna, Maine Coon, Hunger Level: 5
print(dog.pet_status())  # Output: Milo, Cocker Spaniel, Hunger Level: 5

# Feed the dog and play with the cat
dog.feed()
cat.play()

# Check status after actions
print(dog.pet_status())  # Output: Milo, Cocker Spaniel, Hunger Level: 4
print(cat.pet_status())  # Output: Luna, Maine Coon, Hunger Level: 7
