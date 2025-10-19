"""
File: Asset.py
Description: Program to manage Asset class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:

    def __init__(self, name, description, encrypted=False, quantity=1):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted
        self.__quantity = quantity

    def __str__(self):    # managing inventory name, description, status and quantity
        status = "[Encrypted]" if self.__encrypted else ""
        return f"{self.name} - {self.description}\nStatus: {status}\nQuantity: {self.quantity}"

    def get_name(self):
        return self.__name

    def description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    def set_encrypted(self, encrypted):
        return self.__encrypted

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def store_asset(self, amount=1):    # manging increase in asset held inventory
        self.__quantity += amount

    def retrieve_asset(self, amount=1):    # manging increase and decrease in asset held inventory
        if self.__quantity >= amount:
            self.__quantity -= amount
        else:
            print(f"Insufficient {self.name} to retrieve.")

    def display_asset(self):
        return f"{self.name} ({self.quantity}) — {self.description}"

    def get_description(self):
        return self.__description

    # properties to be added
    name = property(get_name)
    description = property(get_description)
    encrypted = property(get_encrypted, set_encrypted)
    quantity = property(get_quantity, set_quantity)


