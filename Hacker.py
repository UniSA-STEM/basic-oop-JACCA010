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
        self.__trace_level = trace_level ["undetected","level 1 - yellow alert", "level 2 - orange alert", "level 3 - red alert", "detected"],
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

            self.__rig input (f"You must first acquire a rig. A rig will cost you one CryptoToken. Do you want to proceed? (Y/N)")

            if self.__rig == "Y":
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

    def trace_level(self):
        while self__hacker_actions == 0:
            self.__trace_level = "undetected"

        if self__hacker_actions == 1:
            self.__trace_level = "level 1 - yellow alert"

        elif self__hacker_actions == 2:
            self.__trace_level = "level 2 - orange alert"

        elif self__hacker_actions == 3:
            self.__trace_level = "level 3 - red alert"

        else:
            self.__trace_level = "detected"

        return self.__trace_level

    def self__hacker_action (self):
        self__hacker_actions +=1

        while self__hacker_actions <=2:
            # all hacker actions available

        if self__hacker_actions ==3:
            # only able to upgrade rig or encrypt assets:

        if self__hacker_actions >=4:
            output = f"{rig.rig_name(self)} has been compromised. You must go underground until your trace level has reduced."

        return self__hacker_actions

    def reduce_trace_level(self, reduce_trace):
        if self.__hacker_actions >=2 and self.hacker_actions !=4:
            self.reduce_trace = input ("Your rig is at risk of being compromised. Further activity will affect your available actions."
                                "Do you want to go underground to reduce your exposure? (Y/N)")
                if reduce_trace == "Y":
                    self.__hacker_actions -= 1

                else:
                    # return to action list with available actions
        else:
            self__hacker_action -= 3
            self.reduce_trace = input ("Your rig is still at risk of being compromised. "
                                       "Do you want to remain underground to reduce your exposure? (Y/N)")
            for self.reduce_trace == "Y":
                self.__hacker_actions -= 1

            else:
                output (f"Proceed at your own risk.")
                    # return to action list with available actions
# action - encrypt assets
# action - rig upgrade
# action - store and retrieve assets /




