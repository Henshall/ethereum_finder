import sys
from time import sleep
import AddressGenerator as AddressGenerator
import random

class MovingLeft:
    
    # constructor
    def __init__(self, stop = False):
        self.stop = stop
        self.AddressGenerator = AddressGenerator.AddressGenerator()
        self.maxIntAllowed = 115792089237316195423570985008687907852837564279074904382605163141518161494336
    
    def process(self, number):
        sleep(0.1)
        numArray = self.number_to_array(number)
        return numArray

    def resetProcess(self, number):
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
    
    def filterNumber(self, number):
        allowNumber = False
        #  number must be less then 2 ^ 256 - 1 billion
        if len(str(number)) > 5:
            if number <  self.maxIntAllowed - 1000000000:
                allowNumber = True
        return allowNumber

    def number_to_array(self, number): 
        # loop 64 times and each time add a 0 to the end of the number and remove it from the front, put the numbers in an array
        privateKeyArray = []
        numberToAdd = number
        firstTimeFlag = True
        for i in range(1, 78):
            if firstTimeFlag == True:
                # remove first character
                numberToAdd = str(numberToAdd)
            else:
                numberToAdd = str(numberToAdd) + "0"

            zfillNumberToAdd = numberToAdd.zfill(64)
            filteredNumber = self.filterNumber(int(zfillNumberToAdd))
            if filteredNumber == True:
                # print("Adding number: " + str(numberToAdd))
                privateKeyofNumber = self.intToPrivateKey( int(zfillNumberToAdd))
                privateKeyArray.append(privateKeyofNumber)
            firstTimeFlag = False

        return privateKeyArray
