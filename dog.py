class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        
my_dog = Dog('Zeus', 7) # instaciate Dog class
my_dog.sit() # Zeus is now sitting.
my_dog.roll_over() # Zeus rolled over
print(my_dog.name)

my_second_dog = Dog('Hans', 5)
my_second_dog.sit()
print(f"Your dog is {my_second_dog.age} years old.")