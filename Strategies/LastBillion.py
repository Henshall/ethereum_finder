import sys
from time import sleep
import AddressGenerator as AddressGenerator

class LastBillion:
    # constructor

    def __init__(self, stop = False):
        self.stop = stop
        self.AddressGenerator = AddressGenerator.AddressGenerator()

    def process(self, number):
        numArray = self.number_to_array(number)
        return numArray

    def resetProcess(self, number):
        # stop at 1 trillion
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
        maxMinusPrivateKeyofNumber = self.intToPrivateKey(self.max_minus_number(number)) 
        return [maxMinusPrivateKeyofNumber]
    
    def max_minus_number(self, number):
        #  note 2 ^ 256, it uses a number less then that 
        #  as shown here https://medium.com/decentralize-today/the-power-of-256-in-blockchain-468aa3f395bc
        # according to SEC standard
         return 115792089237316195423570985008687907852837564279074904382605163141518161494336 - number
    
   
