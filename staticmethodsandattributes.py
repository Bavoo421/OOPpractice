class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# Example usage
result = Calculator.add(5, 7)
print("Sum:", result)
print("Add method called:", Calculator.count, "times")
