"""
File: Hacker.py
Description: Program to manage Hacker class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self, hacker_name, rig=None, trace_level=0, inventory=None, actions=0):
        self.__hacker_name = hacker_name
        self.__rig = rig
        self.__trace_level = trace_level
        self.__inventory = inventory if inventory is not None else [Asset("CryptoToken", "Used to acquire or repair rigs.", "Unencrypted", 1)] # default 1 CryptoToken at start
        self.__actions = actions # number of actions taken (will affect trace level)

    def __str__(self):  # string method added
        rig_status = str(self.__rig) if self.__rig else "No rig assigned"
        self.inventory_list = "\n ".join(str(asset) for asset in self.__inventory) or "Empty"
        trace_description = self.get_trace_level_description()
        output = f"Name: {self.__hacker_name}\nRig: {rig_status}\nTrace Level: {trace_description}\nAssets:\n{self.inventory_list}"

        return output.strip()

    def acquire_rig(self):
        if self.__rig:
           print(f"\nRig acquisition failed: {self.__hacker_name} already has an active rig.")
           print(self.__rig)    # prevent duplication of rig
           return
        assigned_name = self.__hacker_name[:2] + "R" + str(len(self.__hacker_name))
        self.__rig = Rig(assigned_name)    # assigns rig to Hacker
        self.__inventory = [asset for asset in self.__inventory if asset.name != "CryptoToken"]
        print(f"Rig activated. Rig name '{assigned_name}' assigned.\n")
        print(self.scan_inventory())

    def get_trace_level_description(self):
        levels = ["Undetected", "Level 1 - yellow alert", "Level 2 - amber alert", "Level 3 - red alert", "Compromised"]
        return levels[min(self.__trace_level, len(levels))]

    def launch_data_spike(self, target_rig):
        if not self.__rig:
            print(f"No rig assigned to {self.__hacker_name}. Unable to launch Data Spike.\n")
            return

        rig_inventory = self.__rig._Rig__rig_inventory    # accessing the rig inventory
        spike = next((a for a in rig_inventory if a.name == "Data Spike"), None)
        if not spike:
            print(f"You do not have a Data Spike available.\n")
            return

        if self.__trace_level < 2:

            if spike.quantity > 1:
                spike.quantity -= 1
            else:
                rig_inventory.remove(spike)
        else:
            print(f"You cannot perform that action until your trace level has reduced.\n")

        target_rig.take_damage()
        self.__actions += 1
        self.__trace_level += 1

        print(f"Data Spike launched.\n")

    def scan_inventory (self):    # updated to include rig inventory
        output = []
        output.append("Hacker Inventory:")
        if self.__inventory:
            output.extend(f"{asset.display_asset()}" for asset in self.__inventory)
        else:
            output.append("Empty.\n")

        output.append("Rig Inventory:")
        if self.__rig and hasattr(self.__rig, "_Rig__rig_inventory"):
            rig_inventory = self.__rig._Rig__rig_inventory
            if rig_inventory:
                output.extend([f"{asset.display_asset()}" for asset in rig_inventory])
            else:
                output.append("Empty.\n")
        else:
            output.append("(No rig assigned)")

        return "\n".join(output)

    def perform_action(self, action_name):
        self.__actions += 1
        self.__trace_level += 1
        print(f"Action '{action_name}' performed. Trace level: {self.get_trace_level_description()}")

        if self.__trace_level >= 4:
            print(f"{self.__rig.get_rig_name()} has been compromised. You must go underground to reduce exposure.")

    def reduce_trace_level(self):
        if self.__trace_level > 0:
            self.__trace_level -= 1
            print(f"Trace level reduced to: {self.get_trace_level_description()}\n")
        else:
            print("Proceed at your own risk.\n")

    def store_asset(self, new_asset):
        for asset in self.__inventory:
            if asset.name == new_asset.name:
                asset.quantity += new_asset.quantity
                print(f"Updated '{asset.name}' quantity to {asset.quantity} in hacker inventory.")
            return
        self.__inventory.append(new_asset)

    def retrieve_asset(self, asset_name):
        if self.__rig:
            asset = self.__rig.release_asset(asset_name)
            if asset:
                self.__inventory.append(asset)
        else:
            print("Asset not found in inventory.")

    def encrypt_asset(self, asset_name):
        chip = next((a for a in self.__inventory if a.name == "Security Chip"), None)
        if not chip:
            print(f"You do not have a Security Chip available.\n")
            return

        if self.__trace_level < 3:

            if chip.quantity > 1:
                chip.quantity -= 1
            else:
                self.__inventory.remove(chip)
        else:
            print(f"You cannot perform that action until your trace level has reduced.\n")

        asset = next((a for a in self.__inventory if a.name == asset_name), None)    # search hacker inventory

        if not asset and self.__rig and hasattr(self.__rig, "_Rig__rig_inventory"):    #search rig inventory
            asset = next((a for a in self.__rig._Rig__rig_inventory if a.name == asset_name), None)

        if asset:
            asset.encrypted = True
            self.__actions += 1
            self.__trace_level += 1
        else:
            print(f"Asset '{asset_name}' not found in inventory.")

    def decrypt_asset(self, asset_name):
        chip = next((a for a in self.__inventory if a.name == "Security Chip"), None)
        if not chip:
            print(f"You do not have a Security Chip available.\n")
            return

        if self.__trace_level < 3:

            if chip.quantity > 1:
                chip.quantity -= 1
            else:
                self.__inventory.remove(chip)
        else:
            print(f"You cannot perform that action until your trace level has reduced.\n")

        asset = next((a for a in self.__inventory if a.name == asset_name), None)    # search hacker inventory

        if not asset and self.__rig and hasattr(self.__rig, "_Rig__rig_inventory"):    #search rig inventory
            asset = next((a for a in self.__rig._Rig__rig_inventory if a.name == asset_name), None)

        if asset:
            asset.encrypted = False
            self.__actions += 1
            self.__trace_level += 1
        else:
            print(f"Asset '{asset_name}' not found in inventory.")

    def get_rig(self):
        return self.__rig

    def rig_upgrade(self):
        if not self.__rig:
            print(f"No rig assigned to {self.__hacker_name}. Unable to upgrade.")
            return
        upgrade = next((a for a in self.__inventory if a.name == "Hardware Patch"), None)
        if not upgrade or upgrade.quantity < 1:
            print(f"Upgrade failed: Hardware Patch not available.\n")
            return

        if self.__trace_level < 2:
            upgrade.quantity -= 1
            if upgrade.quantity == 0:
                self.__inventory.remove(upgrade)
            self.__rig.upgrade()
        else:
            print(f"You cannot perform that action until your trace level has reduced.\n")

    def rig_repair(self):
        if not self.__rig:
            print(f"No rig assigned to {self.__hacker_name}. No rig to repair.")
            return
        repair = next((a for a in self.__inventory if a.name == "CryptoToken"), None)
        if not repair or repair.quantity < 1:
            print(f"Repair failed: CryptoToken not available.\n")
            return

        repair.quantity -= 1
        if repair.quantity == 0:
            self.__inventory.remove(repair)
            self.__rig.repair()

        else:
            self.__rig_repair(self)
            print(f"Rig has been repaired.\n")

    def extract_assets(self, target_rig):
        if not target_rig or  not hasattr(target_rig, "_Rig__rig_inventory"):
            print(f"Target rig is invalid or inaccessible.")    # checks target rig for valid inventory list.

        rig_inventory = target_rig._Rig__rig_inventory
        if not rig_inventory:
            print(f"Target rig  is empty.")
            return

        for asset in rig_inventory[:]:
            if not asset.encrypted:
                existing = next((a for a in self.__rig._Rig__rig_inventory if a.name == asset.name), None)
                if existing:
                    existing.quantity += asset.quantity
                else:
                    self.__rig._Rig__rig_inventory.append(asset)
            rig_inventory.remove(asset)
            print(f"Transfer of unencrypted assets complete.\n")

# Test extract assets from target rig


enemy_rig = Rig("Midnite")
enemy_hacker = Hacker("RedRose", enemy_rig, 0, None)
target_rig = Rig("DragonFire", 2, "Online", None)
target_hacker = Hacker("BlueDragon", target_rig, 0, None)
enemy_rig.generate_asset(enemy_hacker)
enemy_rig.generate_asset(enemy_hacker)
enemy_rig.generate_asset(enemy_hacker)
enemy_hacker.launch_data_spike(target_rig=target_rig)
print(target_hacker)
enemy_hacker.extract_assets(target_rig)