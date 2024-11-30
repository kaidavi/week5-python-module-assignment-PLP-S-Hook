# week5-python-module-assignment-PLP-S-Hook
Device Class Example
# Smartphone, Tablet, and Device Class Example

This Python program demonstrates the use of object-oriented programming (OOP) concepts such as inheritance, polymorphism, and encapsulation. It features a base `Device` class and two derived classes: `Smartphone` and `Tablet`. Each class is used to model different types of devices and demonstrate how to organize and interact with objects in Python.

## Features
- **Device Class**: A base class representing generic devices with common attributes like `brand`, `model`, and `price`.
- **Smartphone Class**: A derived class that adds attributes specific to smartphones, such as `screen_size` and `battery_life`.
- **Tablet Class**: Another derived class with attributes specific to tablets, such as `screen_size` and `has_stylus`.
- **Encapsulation**: The `price` attribute is encapsulated (protected), and can only be accessed or modified through getter and setter methods.
- **Polymorphism**: Methods like `display_info()` are overridden in derived classes to provide specific behavior for each device type.

## How It Works

1. **Device Class**:
   - Contains common attributes for all devices.
   - Provides methods to display device information and manage the device's price with getter and setter methods.

2. **Smartphone Class**:
   - Inherits from `Device`.
   - Adds smartphone-specific attributes like `screen_size` and `battery_life`.
   - Overrides the `display_info()` method to display more detailed information.
   - Contains a method `use_app()` to simulate using an app on the smartphone.

3. **Tablet Class**:
   - Inherits from `Device`.
   - Adds tablet-specific attributes like `screen_size` and `has_stylus`.
   - Overrides the `display_info()` method to include tablet-specific information.
   - Contains a method `draw()` to simulate drawing with a stylus on the tablet.

4. **Encapsulation**:
   - The `price` attribute is protected (prefixed with `_`), and its value can only be accessed or modified using the `get_price()` and `set_price()` methods.

5. **Polymorphism**:
   - Both the `Smartphone` and `Tablet` classes override the `display_info()` method to provide more detailed and specific information about the device type.

## Example Usage

### Sample Output:

```plaintext
Smartphone Information:
Brand: Apple
Model: iPhone 14
Price: $999
Screen Size: 6.1 inches
Battery Life: 20 hours
Using the Instagram app on your iPhone 14 smartphone...

Tablet Information:
Brand: Samsung
Model: Galaxy Tab S7
Price: $649
Screen Size: 11 inches
Has Stylus: True
Drawing on the screen with the stylus on your Galaxy Tab S7 tablet.

Updated Price for iPhone 14: $1099
