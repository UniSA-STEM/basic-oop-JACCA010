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
    Hacker.acquire_rig()

def test_acquire_duplicate_rig():
    Hacker.acquire_rig()


if __name__ == '__Main__':
    test_hacker_create()



