1. Create a Python class called Product with a private attribute _price. Initialize _price in the constructor and write a method to display its value.

class Product:
    def __init__(self, price):
        self._price = price

    def display_price(self):
        print("Price:", self._price)


product1 = Product(1500)

product1.display_price()

2. Add getter and setter methods for the _price attribute in your Product class to safely access and update the price. Make sure the setter prevents setting a negative price.<br><br><em><strong>Hint:</strong> Raise a ValueError if the new price is less than zero.</em>

class Product:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price


product1 = Product(1500)

print("Current Price:", product1.get_price())

product1.set_price(2000)

print("Updated Price:", product1.get_price())


3. Build a class called Playlist that has a private attribute _songs (a list of song names). Write methods to add a song, remove a song, and get the current list of songs using proper encapsulation.

4. Create an abstract class PaymentMethod with an abstract method pay(amount). Then, create two subclasses: UPI and CreditCard, each implementing the pay method with a print statement showing how the payment would be processed.<br><br><em><strong>Hint:</strong> Use the abc module for abstraction.</em>

from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentMethod):

    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")


class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(f"Processing Credit Card payment of ₹{amount}")


upi_payment = UPI()
card_payment = CreditCard()

upi_payment.pay(500)
card_payment.pay(1000)