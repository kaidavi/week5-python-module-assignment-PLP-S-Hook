# Base class for all moving objects
class MovingObject:
    def move(self):
        pass  # This method will be overridden by subclasses

# Vehicle class representing a car
class Car(MovingObject):
    def move(self):
        print("Driving 🚗")

# Vehicle class representing a plane
class Plane(MovingObject):
    def move(self):
        print("Flying ✈️")

# Animal class representing a dog
class Dog(MovingObject):
    def move(self):
        print("Running 🐕")

# Animal class representing a fish
class Fish(MovingObject):
    def move(self):
        print("Swimming 🐟")

# Animal class representing a bird
class Bird(MovingObject):
    def move(self):
        print("Flying 🦅")

# Function to demonstrate polymorphism
def demonstrate_move(objects):
    for obj in objects:
        obj.move()

# Example of creating instances of the classes
if __name__ == "__main__":
    # Creating objects of different types
    car = Car()
    plane = Plane()
    dog = Dog()
    fish = Fish()
    bird = Bird()

    # List of objects to demonstrate polymorphism
    moving_objects = [car, plane, dog, fish, bird]

    # Demonstrating polymorphism
    print("Demonstrating move() for different objects:")
    demonstrate_move(moving_objects)
