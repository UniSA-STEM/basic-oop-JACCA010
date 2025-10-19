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

def test_asset_generation():
    hacker = Hacker("StarBlaze", None, 0,  None)
    hacker.acquire_rig()    # Acquire Rig
    rig = hacker.get_rig()
    rig.generate_asset(hacker)
    print(hacker.scan_inventory())

def test_multiple_asset_generation():
    hacker = Hacker("StarBlaze", None, 0,  None)
    hacker.acquire_rig()    # Acquire Rig
    rig = hacker.get_rig()
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    print(hacker.scan_inventory())

def test_rig_upgrade():
    hacker = Hacker("SupaNova", None, 0, None)
    hacker.acquire_rig()
    rig = hacker.get_rig()
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    rig.upgrade()
    print(hacker)
    print(hacker.scan_inventory())

def test_trace_level():
    rig = Rig("NsR10")
    hacker = Hacker("NightShadow", rig, 0, None)
    target_rig = Rig("TargetRig", 0, "Online", None)
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    hacker.launch_data_spike(target_rig=target_rig)
    print(hacker.get_trace_level_description())
    print(hacker)

def test_encryption_decryption_base_trace():
    hacker = Hacker("CraterMoon", None, 0, None)
    hacker.acquire_rig()
    rig = hacker.get_rig()
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    print(hacker.scan_inventory())
    hacker.encrypt_asset("Data Spike")
    print(hacker.scan_inventory())
    hacker.rig_upgrade()
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    print(hacker.scan_inventory())
    hacker.decrypt_asset("Hardware Patch")
    print(hacker)
    print(hacker.scan_inventory())

def test_encryption_decryption_trace_2():
    hacker = Hacker("CraterMoon", None, 2, None)
    hacker.acquire_rig()
    rig = hacker.get_rig()
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    print(hacker.scan_inventory())
    hacker.encrypt_asset("Data Spike")
    print(hacker.scan_inventory())
    hacker.rig_upgrade()
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    print(hacker.scan_inventory())
    hacker.decrypt_asset("Hardware Patch")
    print(hacker)
    print(hacker.scan_inventory())

def test_upgrade_high_trace():
    hacker = Hacker("CraterMoon", None, 4, None)
    hacker.acquire_rig()
    rig = hacker.get_rig()
    rig.generate_asset(hacker)
    rig.generate_asset(hacker)
    hacker.rig_upgrade()

def damage_rig():
    enemy_rig = Rig("Midnite")
    enemy_hacker = Hacker("RedRose", enemy_rig, 0, None)
    target_rig = Rig("DragonFire", 2, "Online", None)
    target_hacker = Hacker("BlueDragon", target_rig, 0, None)
    enemy_rig.generate_asset(enemy_hacker)
    enemy_rig.generate_asset(enemy_hacker)
    enemy_rig.generate_asset(enemy_hacker)
    enemy_hacker.launch_data_spike(target_rig=target_rig)
    print(target_hacker)
