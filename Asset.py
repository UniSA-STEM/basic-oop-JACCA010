"""
File: Asset.py
Description: Program to manage Asset class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description, encrypted=False):
        self.__name:  name
        self.__description: description
        self.__encrypted:  encrypted

    def __str__(self):
        status = "Encrypted" if self.encrypted else ""
        return f"{self.name}: {self.description} {status}"
