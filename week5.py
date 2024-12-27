# Assignment 1: Design Your Own Class

# Class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

# Inherited class representing a Gaming Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def play_game(self, game):
        print(f"Playing {game} on {self.model} with {self.gpu} GPU.")

# Creating instances
smartphone = Smartphone("Samsung", "Galaxy S21", 700)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 1000, "Adreno 660")

# Using methods
smartphone.make_call("123-456-7890")
gaming_phone.play_game("PUBG")

# Activity 2: Polymorphism Challenge

class Animal:
    def move(self):
        pass

class Bird(Animal):
    def move(self):
        print("Flying in the sky! 🐦")

class Fish(Animal):
    def move(self):
        print("Swimming in the water! 🐟")

class Cat(Animal):
    def move(self):
        print("Walking gracefully! 🐈")

# Using polymorphism
animals = [Bird(), Fish(), Cat()]
for animal in animals:
    animal.move()
