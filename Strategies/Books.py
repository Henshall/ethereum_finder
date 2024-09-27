import sys
from time import sleep
import AddressGenerator as AddressGenerator

class Books:
    # constructor

    def __init__(self, stop = False):
        self.stop = stop
        self.AddressGenerator = AddressGenerator.AddressGenerator()
        print("Books instantiated")
        # load books from books/all_books.txt
        self.book = open("books/all_books.txt", "r")
        self.book = self.book.read()
        self.book_length = len(self.book)


    def process(self, number):
        numArray = self.number_to_array(number)
        return numArray

    def resetProcess(self, number):
        if number > self.book_length - 500:
            return True
        else:
            return False
        
        
    def number_to_array(self, number):
        # get 200 characters depending on where counter is. Also get the string without spaces
        stringToCheck = self.book[number:number+200]
        stringToCheckWithoutSpaces = stringToCheck.replace(" ", "")
        # generate private keys from strings
        privateKeysFromString = self.AddressGenerator.generate_private_keys_from_string(stringToCheck)
        privateKeysFromStringWithoutSpaces = self.AddressGenerator.generate_private_keys_from_string(stringToCheckWithoutSpaces)
        # merge arrays and make them unique
        privateKeysArray = list(set(privateKeysFromString + privateKeysFromStringWithoutSpaces))
        # return array
        return privateKeysArray

