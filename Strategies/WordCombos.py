import sys
from time import sleep
import AddressGenerator as AddressGenerator


class WordCombos:
    # constructor

    def __init__(self, stop = False):
        self.stop = stop
        self.AddressGenerator = AddressGenerator.AddressGenerator()
        print("EncodeWords instantiated")
        # load books from books/all_books.txt
        self.all_words = open("books/all_english_words.txt", "r")
        self.all_words = self.all_words.read()
        self.all_words_array = self.all_words.split("\n")
        self.all_words_array_length = len(self.all_words_array)

    def process(self, number):
        numArray = self.number_to_array(number)
        return numArray
    
    def resetProcess(self, number):
    # stop at 1 billion
        if number > 1000000000:
            return True
        else:
            return False

    def number_to_array(self, number):
        possible_combinations_one_word = self.all_words_array_length
        # determine number of possible 2 word combinations from: self.all_words_array_length
        possible_combinations_two_words = self.all_words_array_length ** 2
        # determine number of possible 3 word combinations from: self.all_words_array_length
        possible_combinations_three_words = self.all_words_array_length ** 3
        # determine number of possible 4 word combinations from: self.all_words_array_length

        # if number is less than the number of possible combinations of one word
        if number < possible_combinations_one_word - 1000:
            oneWord = self.all_words_array[number]
            oneWordArray = self.wordCombosArrayIntoStringsArray([oneWord])
        else:
            oneWordArray = []

        if number < possible_combinations_two_words - 1000:
            twoWordCombos = self.generate2WordsFromNumber(number)
            twoWordCombosArray = self.wordCombosArrayIntoStringsArray(twoWordCombos)
        else:
            twoWordCombosArray = []

        if number < possible_combinations_three_words - 1000:
            threeWordCombos = self.generate3WordsFromNumber(number)
            threeWordCombosArray = self.wordCombosArrayIntoStringsArray(threeWordCombos)
        else:
            threeWordCombosArray = []
        
        # merge all of the arrays
        allCombosArray = oneWordArray + twoWordCombosArray + threeWordCombosArray
 
        privateKeysArray = []
        # /use generate_private_keys_from_string 
        for combo in allCombosArray:
            privateKeys = self.AddressGenerator.generate_private_keys_from_string(combo)
            privateKeysArray += privateKeys

        # make sure private keys array is unique
        privateKeysArray = list(set(privateKeysArray))

        return(privateKeysArray)
        

    def wordCombosArrayIntoStringsArray(self, wordCombos):
        wordCombosString = " ".join(wordCombos)
        wordCombosStringNoSpaces = wordCombosString.replace(" ", "")
        wordCombosStringUnderscore = wordCombosString.replace(" ", "_")
        wordCombosStringLower = wordCombosString.lower()
        wordCombosStringNoSpacesLower = wordCombosStringNoSpaces.lower()
        wordCombosStringUnderscoreLower = wordCombosStringUnderscore.lower()
        return [wordCombosString, wordCombosStringNoSpaces, wordCombosStringUnderscore, wordCombosStringLower, wordCombosStringNoSpacesLower, wordCombosStringUnderscoreLower]

    def generate2WordsFromNumber(self, number):
        base = self.all_words_array_length

        indices = []
        for _ in range(2):
            indices.append(number % base)
            number //= base

        words = [self.all_words_array[index] for index in indices]
        return words 

    def generate3WordsFromNumber(self, number):
        base = self.all_words_array_length

        indices = []
        for _ in range(3):  # We need 3 indices
            indices.append(number % base)
            number //= base
        
        words = [self.all_words_array[index] for index in indices]
        return words
    