"""
File: Rig.py
Description: Program to manage Rig class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from asset import Asset

class Rig:

    def __init__(self, rig_name, damage=0, rig_status="Online", rig_inventory=None, upgrade_level=0, max_damage=2):
        self.__rig_name = rig_name  #get hacker_name
        self.__damage = damage
        self.__rig_status = rig_status
        self.__rig_inventory = rig_inventory if rig_inventory is not None else []
        self.__upgrade_level = upgrade_level  #default 0
        self.__max_damage = max_damage  #max_damage 2 before rig status = critical damage - rig offline

    def __str__(self):
        inventory_list = "\n  ".join(str(asset) for asset in self.__rig_inventory) or "Empty"
        return f"Rig Name: {self.__rig_name}\nStatus: {self.__rig_status}\nDamage: {self.__damage}/{self.__max_damage}\nUpgrade Level: {self.__upgrade_level}\nInventory:\n{inventory_list}"


    def get_rig_name(self):
        return self.__rig_name

    def get_status(self):
        return self.__rig_status

    def get_damage(self):
        return self.__damage

    def get_upgrade_level(self):
        return self.__upgrade_level

    def set_rig_name(self,name):
        self.__rig_name = name

    def take_damage(self, amount=1):
        self.__damage += amount
        if self.__damage >= self.__max_damage:
            self.__rig_status = "Critical Damage - Unit Offline"
        else:
            self.__rig_status = "Damaged"

        print(f"{self.__rig_name} has {self.__damage}/{self.__max_damage} damage.\nStatus: {self.__rig_status}")

    def repair(self):
        if self.__damage >0:
            self.__damage -= 1
            self.__rig_status = "Online" if self.__damage == 0 else "Damaged"
            print (f"{self.__rig_name} repaired.\nDamage: {self.__damage}")
        else:
            print (f"{self.__rig_name} is fully operational.")

    def upgrade(self):
        self.__upgrade_level += 1
        print(f"{self.__rig_name} upgraded to level {self.__upgrade_level}")

    def store_asset(self, asset):
        self.__rig_inventory.append(asset)
        print(f"Asset '{asset.name}' stored in {self.__rig_name}.")

    def release_asset(self, asset_name):
        for asset in self.__rig_inventory:
            if asset.name == asset_name:
                self.__rig_inventory.remove(asset)
                print(f"Asset '{asset.name}' released from {self.__rig_name}.")
                return asset
        print(f"Asset '{asset_name}' not found in {self.__rig_name}.")
        return None


