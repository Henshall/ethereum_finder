import sys
from time import sleep
import AddressGenerator as AddressGenerator
import random

class AllBinary:
    
    # constructor
    def __init__(self, stop = False):
        self.stop = stop
        self.AddressGenerator = AddressGenerator.AddressGenerator()
    
    def process(self, number):
        numArray = self.number_to_array(number)
        return numArray

    def resetProcess(self, number):
        if number > 100000000000000:
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
        # find the first private key:
        # starts at 10000 which is around a trilltion because this amount converted to binary
        # will be covered in the FirstTrillion class
        BinaryNumber = bin(number + 10000)[2:]
        binaryInt = int(BinaryNumber)
        firstPrivateKey = self.intToPrivateKey(binaryInt)

        # now we find the second private key
        # instead of having zeros to the left of the binary number, we will have zeros to the right
        secondBinaryNumber =  bin(number)[2:]
        stringOfSecondBinaryNumber = str(secondBinaryNumber)
        secondBinaryNumberRightFilled =  stringOfSecondBinaryNumber.ljust(78, '0')
        binaryNumberRightFilledInt = int(secondBinaryNumberRightFilled)
        # print("BinaryNumber: " + str(BinaryNumber))
        # print("secondBinaryNumberRightFilled: " + str(secondBinaryNumberRightFilled))
        privateKeyofNumber2 = self.intToPrivateKey(binaryNumberRightFilledInt)
        return [firstPrivateKey, privateKeyofNumber2]
        


