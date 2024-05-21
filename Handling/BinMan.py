import weakref
from Runner.ZenoneClasses import Zenone
import time
class BinMan:
    instances = []

    @classmethod
    def add_to_bin(cls, rubbish):
        cls.instances.append(rubbish)

    @classmethod
    def put_in_bin_truck(cls):
        cls.instances = [rubbish for rubbish in cls.instances if rubbish is not None]
    @classmethod
    def incinerate(cls, rubbish):
        if rubbish in cls.instances:
            cls.instances.remove(rubbish)
            del rubbish

def BinManCall(amount, timing):
    for i in range(amount):
        time.sleep(timing)
        rubbish = Zenone()
        BinMan.add_to_bin(rubbish)
        BinMan.put_in_bin_truck()
        BinMan.incinerate(rubbish)
