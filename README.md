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


# Moving Objects Program

This Python program demonstrates **polymorphism** through a collection of animal and vehicle classes, each implementing their own version of the `move()` method. While each class shares the same method name (`move()`), each one defines its behavior differently to simulate various types of movement.

### Key Concepts Covered:
- **Polymorphism**: Different classes can implement a method with the same name (`move()`) but different behavior.
- **Inheritance**: The base class `MovingObject` is inherited by subclasses like `Car`, `Plane`, `Dog`, `Fish`, and `Bird`.
- **Method Overriding**: Each subclass overrides the `move()` method to provide its own unique implementation.

## Classes

### 1. `MovingObject` (Base Class)
This is the base class that other classes inherit from. It defines an empty `move()` method, which is overridden in each subclass.

### 2. `Car`
- **Method**: `move()`
- **Description**: Prints `"Driving 🚗"` to simulate car movement.

### 3. `Plane`
- **Method**: `move()`
- **Description**: Prints `"Flying ✈️"` to simulate plane movement.

### 4. `Dog`
- **Method**: `move()`
- **Description**: Prints `"Running 🐕"` to simulate a dog's movement.

### 5. `Fish`
- **Method**: `move()`
- **Description**: Prints `"Swimming 🐟"` to simulate a fish's movement.

### 6. `Bird`
- **Method**: `move()`
- **Description**: Prints `"Flying 🦅"` to simulate a bird's movement.

## Example Usage

### Sample Output:
```plaintext
Demonstrating move() for different objects:
Driving 🚗
Flying ✈️
Running 🐕
Swimming 🐟
Flying 🦅
