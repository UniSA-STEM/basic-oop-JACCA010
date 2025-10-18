"""
File: Asset.py
Description: Program to manage Asset class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:

    asset_list = {
        "CryptoToken": "Used to acquire or repair rigs.",
        "Data Spike": "Used in battles.",
        "Removable Drive": "Found in rigs and used for extraction.",
        "Security Chip": "Used to encrypt or decrypt assets.",
        "Hardware Patch": "Used to upgrade rigs.",
    }

    def __init__(self, name, description, encrypted=False, quantity=0):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted
        self.__quantity = quantity

    def __str__(self):    # managing inventory name, description, status and quantity
        return f"{self.name} - {self.description}\nStatus: {self.encrypted}\nQuantity: {self.quantity}"

    def get_name(self):
        return self.__name

    def description(self):
        return self.__description

    def get_encrypted(self):
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
        status = "Encrypted" if self.encrypted else "Unencrypted"
        return f"{self.name} ({self.quantity}) — {self.description} [{status}]"




    # properties to be added
    name = property(get_name)
    description = property(description)
    encrypted = property(get_encrypted)
    quantity = property(get_quantity)


