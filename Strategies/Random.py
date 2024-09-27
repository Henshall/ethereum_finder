import sys
from time import sleep
import AddressGenerator as AddressGenerator
import random

class Random:
    # constructor
    def __init__(self, stop = False):
        self.stop = stop
        self.AddressGenerator = AddressGenerator.AddressGenerator()
        self.maxIntAllowed = 115792089237316195423570985008687907852837564279074904382605163141518161494336

    def process(self, number):
        numArray = self.number_to_array(number)
        return numArray

    def resetProcess(self, number):
        if number > 100000000:
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
        if len(str(number)) > 8:
            if number <  self.maxIntAllowed - 1000000000:
                allowNumber = True
        return allowNumber
        
    def number_to_array(self, number): 
        FilteredRandomNumber = self.generateFilteredRandomNumber()
        a78CharacterRandomNumber = self.generate78CharacterRandomNumber()
        randomNumberArray = self.generateRandomNumberArray()
        # merge the arrays
        randomNumberArray.append(FilteredRandomNumber)
        randomNumberArray.append(a78CharacterRandomNumber)

        # convert the numbers to private keys
        privateKeyArray = []
        for randomNumber in randomNumberArray:
            privateKey = self.intToPrivateKey(randomNumber)
            privateKeyArray.append(privateKey)

        return privateKeyArray

    # generate a random number
    def generateFilteredRandomNumber(self):
        randomNumber = random.randint(1000000000, self.maxIntAllowed)
        return randomNumber

    # generate a random number which takes up all 78 characters
    def generate78CharacterRandomNumber(self):
        minimumNumber = 100000000000000000000000000000000000000000000000000000000000000000000000000000
        randomNumber = random.randint(minimumNumber, self.maxIntAllowed)
        return randomNumber

    def generateRandomNumberArray(self):
        counter = 0
        numbersArray = []
        # while counter is less than 100
        while counter < 90:
            counter = counter + 1
            randomNumber = self.generateRandomNumberOfXLength(counter)
            # filter number
            filterNumber = self.filterNumber(randomNumber)
            if filterNumber == True:
                numbersArray.append(randomNumber)
        return numbersArray
    
    def generateRandomNumberOfXLength(self, length):
        length = int(length)
        # generate a random number of a certain length
        maximumNumber = 10 ** length
        minimumNumber = maximumNumber / 10
        randomNumber = random.randint(minimumNumber, maximumNumber)
        return int(randomNumber)
