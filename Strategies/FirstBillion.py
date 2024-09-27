import sys
from time import sleep
import AddressGenerator as AddressGenerator

class FirstBillion:
    # constructor

    def __init__(self, stop = False):
        print("FirstBillion instantiated")
        self.stop = stop
        self.AddressGenerator = AddressGenerator.AddressGenerator()

    def process(self, number):
        numArray = self.number_to_array(number)
        return numArray

    def resetProcess(self, number):
        # stop at 1 billion
        if number > 1000000000:
            return True
        else:
            return False
        
    def intToPrivateKey(self, number):
        try:
            return self.AddressGenerator.int_to_private_key(number)
        except:
            print("Error generating address from int: " + str(number))
            return"0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140"
        
    def number_to_array(self, number):
        privateKeyofNumber = self.intToPrivateKey(number)
        return [privateKeyofNumber]
    