"""
File: Asset.py
Description: Program to manage Asset class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self):
        self.__asset_name:  ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]
        self.__asset_description: []    # list of lists?
        self.__attribute:  "Unencrypted"    # default setting
        self.__inventory_type: ""    # hacker or rig inventory

    # asset descriptions as per COMP1048 instructions
    # actions to be created to move between hacker and rig inventory lists
    # actions to be created to add or delete certain assets based on utilisation
