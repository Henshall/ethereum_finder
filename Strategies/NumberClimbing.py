import sys
from time import sleep
import AddressGenerator as AddressGenerator

class NumberClimbing:
    # constructor

    def __init__(self, stop = False):
        self.stop = stop
        self.AddressGenerator = AddressGenerator.AddressGenerator()
        self.maxIntAllowed = 115792089237316195423570985008687907852837564279074904382605163141518161494336
        

    def process(self, number):
        numArray = self.number_to_array(number)
        return numArray

    def resetProcess(self, number):
        if number > 10000000:
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
        privateKeysArray = []
        repeatNumbersArray = self.generateRepeatNumbersArray(number)
        for repeatNumber in repeatNumbersArray:
            privateKeysArray.append(self.intToPrivateKey(repeatNumber))
        
        return privateKeysArray
    
    def generateRepeatNumbersArray(self, number):
        counter = 0
        numbersArray = []
        globalNumberString = ""
        while len(str(globalNumberString)) < 90:
            counter = counter + 1
            globalNumberString = globalNumberString + str(number + counter)
            if self.filterNumber(int(globalNumberString)) == True:
                numbersArray.append(int(globalNumberString))

        return numbersArray
