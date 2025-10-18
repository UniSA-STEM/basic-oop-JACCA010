"""
File: Hacker.py
Description: Program to manage Hacker class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from asset import Asset
from rig import Rig

class Hacker:
    def __init__(self, hacker_name, rig=None, trace_level=0, inventory=None, actions=0):
        self.__hacker_name = hacker_name
        self.__rig = rig
        self.__trace_level = trace_level  # list to be defined
        self.__inventory = inventory if inventory is not None else [Asset("CryptoToken", "Used to acquire or repair rigs")]  # default 1 CryptoToken at start
        self.__actions = actions # number of actions taken (will affect trace level)

    def __str__(self):  # string method added
        rig.rig_status = str(self.__rig) if self.__rig else "No rig assigned"
        self.inventory_list = "\n ".join(str(asset) for asset in self.__inventory) or "Empty"
        self.trace_description = self.get_trace_level_description()
        output = f"Name: {self.__hacker_name}\nRig: {self.__rig}\nTrace Level: {self.__trace_level}\nAssets: {self.__inventory}"
        return output.strip()

    def acquire_rig(self, rig=None, rig_name=None):
        if "CryptoToken" in [asset.name for asset in self.__inventory]:
            confirm = input("Acquiring a rig costs one CryptoToken. Proceed? (Y/N): ")
            if confirm.upper() == "Y":
                if rig_name is None:
                    rig.rig_name = self.__hacker_name[:2] + "R" + str(len(self.__hacker_name))
                    self.__inventory = [asset for asset in self.__inventory if asset.name != "CryptoToken"]
                    print(f"Rig activated. Rig name '{rig_name}' assigned.")
            else:
                print("Rig acquisition cancelled.")
        else:
            print("No CryptoToken available to acquire rig.")

    def get_trace_level_description(self):
        levels = ["Undetected", "Level 1 - yellow alert", "Level 2 - amber alert", "Level 3 - red alert", "Compromised"]
        return levels[min(self.__trace_level, len(levels)) - 1]




    def launch_data_spike(self, target_rig):
        spike = next((a for a in self.__inventory if a.name == "Data Spike"), None)
        if not spike:
            print("You do not have a Data Spike available.")
            return
        self.__inventory.remove(spike)
        target_rig.take_damage()
        self.__actions += 1
        self.__trace_level += 1
        print(f"Data Spike launched. Trace level now: {self.get_trace_level_description()}")

    def scan_inventory (self):    # show current inventory details for hacker
        return "\n".join(str(asset) for asset in self.__inventory) or "Inventory is empty."

    def trace_level(self):
        while self.__actions == 0:
            self.__trace_level = "undetected"

        if self.__actions == 1:
            self.__trace_level = "level 1 - yellow alert"

        elif self.__actions == 2:
            self.__trace_level = "level 2 - orange alert"

        elif self.__actions == 3:
            self.__trace_level = "level 3 - red alert"

        else:
            self.__trace_level = "detected"

        return self.__trace_level

    def perform_action(self, action_name):
        self.__actions += 1
        self.__trace_level += 1
        print(f"Action '{action_name}' performed. Trace level: {self.get_trace_level_description()}")

        if self.__trace_level >= 4:
            print(f"{self.__rig.get_rig_name()} has been compromised. You must go underground to reduce exposure.")

    def reduce_trace_level(self):
        if self.__trace_level > 0:
            confirm = input("Do you want to go underground to reduce your trace level? (Y/N): ")
            if confirm.upper() == "Y":
                self.__trace_level -= 1
                print(f"Trace level reduced to: {self.get_trace_level_description()}")
        else:
            print("Proceed at your own risk.")

    def store_asset(self, asset_name):
        asset = next((a for a in self.__inventory if a.name == asset_name), None)
        if asset and self.__rig:
            self.__rig.store_asset(asset)
            self.__inventory.remove(asset)
        else:
            print(f"Rig upgrade required, cannot store asset '{asset_name}")


    def retrieve_asset(self, asset_name):
        if self.__rig:
            asset = self.__rig.release_asset(asset_name)
            if asset:
                self.__inventory.append(asset)
        else:
            print("Asset not found in inventory.")

    def encrypt_asset(self, asset_name):
        asset = next((a for a in self.__inventory if a.name == asset_name), None)
        if asset:
            asset.encrypt()
        else:
            print(f"Asset '{asset_name}' not found in inventory.")

    def decrypt_asset(self, asset_name):
        asset = next((a for a in self.__inventory if a.name == asset_name), None)
        if asset:
            asset.decrypt()
        else:
            print(f"Asset '{asset_name}' not found in inventory.")

import asset
print(asset.Asset("Test", "Just testing"))