#!/usr/bin/env python

from Runner.ZenoneRunner import *
from Runner.ZenoneClasses import *
from Handling.BinMan import BinMan, BinManCall
import os
import sys
import weakref
import time

def main(file_path):
    try:
        with open(file_path, "r") as file:
            BinManCall(1, 0.00001)
            Runner(file_path)
            BinManCall(1, 0)
    except FileNotFoundError:
        FileError(file_path)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Zenone Script Incomplete Run Statement: `zenone.py <script>.zne`")
        sys.exit(1)

    file_path = sys.argv[1]
    if not file_path.endswith(".zne"):
        print("Error: File must have a .zne extension")
        sys.exit(1)

main(file_path)
