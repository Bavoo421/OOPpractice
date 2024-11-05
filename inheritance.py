class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Example usage
dog = Dog()
dog.eat()
dog.sleep()
dog.bark()
