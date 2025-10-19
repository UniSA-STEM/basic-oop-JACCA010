"""
File: main.py
Description: Program to manage the classes and test program as part of COMP1048 Basic Programming Assessment
Author: Catherine Jackson
ID: 110481962
Username: JACCA010
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Rig import Rig
from Asset import Asset

# Initiate test cases

def test_hacker_create():
    hacker = Hacker ("DragonFire", None, 0, None)
    print(hacker)

def test_acquire_rig():
    hacker = Hacker("DragonFire", None, 0, None)
    hacker.acquire_rig()
    print(hacker)

def test_acquire_duplicate_rig():
    hacker = Hacker("DragonFire", None, 0, None)
    hacker.acquire_rig()
    hacker.acquire_rig()
    print(hacker)

def test_no_data_spike():
    hacker = Hacker("DragonFire", None, 0, None)
    hacker.acquire_rig()
    hacker.launch_data_spike()
    print(hacker)

def test_no_hardware_patch():
    hacker = Hacker("DragonFire", None, 0, None)
    hacker.acquire_rig()
    hacker.rig_upgrade()
    print(hacker)

def test_generate_asset():
    hacker = Hacker("DragonFire", None, 0, None)    # No rig yet
    hacker.acquire_rig()    # Acquire Rig

    rig = hacker.get_rig()    # Access rig instance

    rig.generate_asset(hacker)    # Initiate random asset generation

    print("Hacker Inventory:")
    print(hacker.scan_inventory())

    print("\nRig Inventory:")
    print(rig.scan_inventory())


