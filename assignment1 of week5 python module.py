# Base class representing a generic device
class Device:
    def __init__(self, brand, model, price):
        self.brand = brand        # Public attribute
        self.model = model        # Public attribute
        self._price = price       # Protected attribute (intended for internal use)
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self._price}")

    def get_price(self):
        # Getter method for price (encapsulation)
        return self._price

    def set_price(self, new_price):
        # Setter method for price (encapsulation)
        if new_price > 0:
            self._price = new_price
        else:
            print("Invalid price!")

# Inherited class representing a smartphone
class Smartphone(Device):
    def __init__(self, brand, model, price, screen_size, battery_life):
        super().__init__(brand, model, price)  # Initialize the base class
        self.screen_size = screen_size  # Additional attribute for smartphones
        self.battery_life = battery_life  # Additional attribute for smartphones
    
    def display_info(self):
        # Overriding the base class method (polymorphism)
        super().display_info()  # Call the base class display_info
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Battery Life: {self.battery_life} hours")

    def use_app(self, app_name):
        print(f"Using the {app_name} app on your {self.model} smartphone...")

# Inherited class representing a tablet (another kind of device)
class Tablet(Device):
    def __init__(self, brand, model, price, screen_size, has_stylus):
        super().__init__(brand, model, price)  # Initialize the base class
        self.screen_size = screen_size  # Additional attribute for tablets
        self.has_stylus = has_stylus  # Additional attribute for tablets
    
    def display_info(self):
        # Overriding the base class method (polymorphism)
        super().display_info()  # Call the base class display_info
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Has Stylus: {self.has_stylus}")
    
    def draw(self):
        if self.has_stylus:
            print(f"Drawing on the screen with the stylus on your {self.model} tablet.")
        else:
            print(f"Cannot draw on the screen because your {self.model} tablet does not have a stylus.")

# Example of creating instances of the classes
if __name__ == "__main__":
    smartphone = Smartphone("Apple", "iPhone 14", 999, 6.1, 20)
    tablet = Tablet("Samsung", "Galaxy Tab S7", 649, 11, True)

    print("\nSmartphone Information:")
    smartphone.display_info()
    smartphone.use_app("Instagram")

    print("\nTablet Information:")
    tablet.display_info()
    tablet.draw()

    # Using encapsulation to modify the price
    smartphone.set_price(1099)
    print(f"\nUpdated Price for {smartphone.model}: ${smartphone.get_price()}")
