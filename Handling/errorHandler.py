import os
from Runner.ZenoneRunner import *

current_file = __file__
file_path = os.path.abspath(__file__)


def FileError(file_path):
    print(f"File '{file_path}' Not Found")
    print(f"Check Spelling/Directory/Existence Of File '{file_path}'")
