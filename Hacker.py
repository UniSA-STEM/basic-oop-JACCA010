"""
File: Hacker.py
Description: Program to manage Hacker class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Hacker:
    def __init__(self, hacker_name, rig, trace_level, inventory, hacker_actions):
        self.__hacker_name = hacker_name
        self.__rig = rig
        self.__trace_level = trace_level ["undetected","level 1 - alert", "level 2 - high alert", "level 3 - detected"],
        self.__inventory = inventory if inventory is not None else []
        self.__hacker_actions = hacker_actions ["launch_data_spike""encrypt_assets","upgrade_rig","store_assets","retrieve_assets"]

    def __str__(self):  # string method added
        output = f"Name: {self.__hacker_name}\nRig: {self.__rig}\nTrace Level: {self.__trace_level}\nAssets: {self.__inventory}"
        return output.strip()

    def hacker_name(self):
        self.__hacker_name = input(f"What is your name?")
        return self.__hacker_name

    def acquire_rig (self, rig=None, rig_name=None, inventory = "CryptoToken" ):    # method to initiate rig for new hacker
        if self.__rig == None:
            rig.set_rig_name = self.__hacker_name[0,1] + "R" + len(self.__hacker_name)
            asset.set_inventory(inventory)
            self.__inventory.remove(inventory)

            input (f"You must first acquire a rig. A rig will cost you one CryptoToken. Do you want to proceed? (Y/N)")

            if input() == "Y":

               rig.set_rig_name(rig_name)


            else:
                input (f"You must first acquire a rig. A rig will cost you one CryptoToken. Do you want to proceed? (Y/N)")

        print(f"Rig activated. Rig name {rig_name} assigned.")  # add rig.set_rig_name method

    def launch_data_spike(self):

        target_rig = ()    # need to define target_rig
        target_rig_damage = ()    # get rig info on target rig
        data_spike = 1     #    add method to check inventory for number of data spikes

        if data_spike == 0:
            print (f"You do not have sufficient data spikes available.")

        else:
            data_spike -= 1
            target_rig_damage += 1    #target_rig_damage to be defined

        #    add method to return to activity screen


    def scan_inventory (self):    # show current inventory details for hacker
        output_inventory = f"{self.__inventory}"
        return output_inventory.strip()

# action - encrypt assets
# action - rig upgrade
# action - store and retrieve assets /



