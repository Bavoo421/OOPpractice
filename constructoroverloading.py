class Rectangle:
    def __init__(self, width, height=None):
        if height is None:  # Single argument indicates a square
            height = width
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
square = Rectangle(5)
rectangle = Rectangle(4, 6)
print("Square area:", square.area())
print("Rectangle area:", rectangle.area())
