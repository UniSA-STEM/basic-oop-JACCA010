"""
File: Rig.py
Description: Program to manage Rig class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:

    def __init__(self, rig_name, damage, rig_status, rig_inventory, upgrade_level, max_damage=2):
        self.__rig_name = rig_name  #get hacker_name
        self.__damage = damage
        self.__rig_status = rig_status
        self.__rig_inventory = rig_inventory
        self.__upgrade_level = upgrade_level  #default 0
        self.__max_damage = max_damage  #max_damage 2 before rig status = critical damage - rig offline

    def set_rig_name(self):
        return self.__rig_name





    # repair action to be added
    # upgrade action to be added
    # transfer of inventory between rig and hacker to be added
    # asset generation (random) to be added
    # rig damage to be added max damage = 2