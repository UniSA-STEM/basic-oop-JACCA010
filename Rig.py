"""
File: Rig.py
Description: Program to manage Rig class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self):
        self.__rig_name = ""    # Linked to hacker name?
        self.__damage = 0
        self.__condition = ""    # Based on damage level
        self.__storage = ""    # Rig inventory with default inclusions
        self.__upgrade_level = 0    # default level
        self.__max_damage = 2

    # repair action to be added
    # upgrade action to be added
    # transfer of inventory between rig and hacker to be added
    # asset generation (random) to be added
    # rig damage to be added max damage = 2