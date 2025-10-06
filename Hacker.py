"""
File: Hacker.py
Description: Program to manage Hacker class as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Hacker:

    def __init__(self, name, rig, trace_level, inventory):
        self._name = []  # possible random name creation?
        self.__rig = []  # consider option to use hacker name?
        self.__trace_level = 0  # exposure level baseline
        self.__inventory = ""  # get asset?

    def __str__(self):  # string method added
        output = f"{self._name}, {self.__rig}, {self.__trace_level}, {self.__inventory}"
        return output.strip()


    def acquire_rig (self):    # method to initiate rig for new hacker
        if self.__rig == None:
            input (f"You must first acquire a rig. A rig will cost you one CryptoToken. Do you want to proceed? (Y/N)")
            if input() == "Y":

                #    Add method to reduce CryptoToken by 1

                print (f"Rig activated. Rig name {self.__rig} assigned.")

            else:
                input (f"You must first acquire a rig. A rig will cost you one CryptoToken. Do you want to proceed? (Y/N)")
        else:
            return self.__rig

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
