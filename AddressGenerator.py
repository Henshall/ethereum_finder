from eth_keys import keys
from eth_utils import decode_hex
import hashlib
from hashlib import sha256

class AddressGenerator:

    def __init__(self):
        print("AddressGenerator instantiated")
        self.maxIntAllowed = 115792089237316195423570985008687907852837564279074904382605163141518161494336

    # this function turns an integer into a private key
    def int_to_private_key(self, n):
        hexOfInt = hex(n)
        hex64Filled = hexOfInt[2:].zfill(64)
        # print("Hex64Filled: " + str(hex64Filled))
        decodedHex = decode_hex(hex64Filled)
        # print("Decoded Hex: " + str(decodedHex))
        privateKey = keys.PrivateKey(decodedHex)
        # print("Private Key: " + str(privateKey))    
        return privateKey
    
    # this function turns a private key into a public key
    def private_key_to_public_key(self, priv_key):
        return priv_key.public_key

    # this function turns a public key into an address
    def public_key_to_address(self, pub_key):
        return pub_key.to_checksum_address()

    # this function takes in an integer and returns an address
    # only integers lower than 115792089237316195423570985008687907852837564279074904382605163141518161494336 are allowed
    # integers over this number will fail.
    def generate_address_from_int(self, n):
        # print ("Generating address from int: " + str(n))    
        priv_key = self.int_to_private_key(n)
        # print ("Private Key: " + str(priv_key))
        pub_key = self.private_key_to_public_key(priv_key)
        # print ("Public Key: " + str(pub_key))
        address = self.public_key_to_address(pub_key)
        # print ("Address: " + str(address))
        return address
    
    def generate_address_from_private_key(self, priv_key):
        pub_key = self.private_key_to_public_key(priv_key)
        address = self.public_key_to_address(pub_key)
        return address
    

    # ////////////////////////////////////////

    
    # create a function to generate an address from a string
    def generate_private_keys_from_string(self, string):
        
        # Encode the string in various formats
        encoded_bytes_utf8 = string.encode('utf-8')
        
        try:
            encoded_bytes_ascii = string.encode('ascii')
        except:
            encoded_bytes_ascii = string.encode('utf-8')
        
        encoded_bytes_utf16 = string.encode('utf-16')
        encoded_bytes_utf32 = string.encode('utf-32')

        try:
            encoded_bytes_latin_1 = string.encode('latin-1')
        except:
            encoded_bytes_latin_1 = string.encode('utf-8')

        try:
            encoded_bytes_cp1252 = string.encode('cp1252')

        except:
            encoded_bytes_cp1252 = string.encode('utf-8')


        try:
            encoded_bytes_iso_8859_2 = string.encode('iso-8859-2')
        except:
            encoded_bytes_iso_8859_2 = string.encode('utf-8')

        try:
            encoded_bytes_gbk = string.encode('gbk')
        except:
            encoded_bytes_gbk = string.encode('utf-8')

        try:
            encoded_bytes_shift_jis = string.encode('shift_jis')
        except:
            encoded_bytes_shift_jis = string.encode('utf-8')

        # Slice the first 32 bytes of each encoding
        first_32_bytes_utf8 = encoded_bytes_utf8[:32]
        first_32_bytes_ascii = encoded_bytes_ascii[:32]
        first_32_bytes_utf16 = encoded_bytes_utf16[:32]
        first_32_bytes_utf32 = encoded_bytes_utf32[:32]
        first_32_bytes_latin_1 = encoded_bytes_latin_1[:32]
        first_32_bytes_cp1252 = encoded_bytes_cp1252[:32]
        first_32_bytes_iso_8859_2 = encoded_bytes_iso_8859_2[:32]
        first_32_bytes_gbk = encoded_bytes_gbk[:32]
        first_32_bytes_shift_jis = encoded_bytes_shift_jis[:32]

        # Convert each encoding into an integer
        int_value_little_utf8 = int.from_bytes(first_32_bytes_utf8, 'little')
        int_value_big_utf8 = int.from_bytes(first_32_bytes_utf8, 'big')
        int_value_little_ascii = int.from_bytes(first_32_bytes_ascii, 'little')
        int_value_big_ascii = int.from_bytes(first_32_bytes_ascii, 'big')
        int_value_little_utf16 = int.from_bytes(first_32_bytes_utf16, 'little')
        int_value_big_utf16 = int.from_bytes(first_32_bytes_utf16, 'big')
        int_value_little_utf32 = int.from_bytes(first_32_bytes_utf32, 'little')
        int_value_big_utf32 = int.from_bytes(first_32_bytes_utf32, 'big')
        int_value_little_latin_1 = int.from_bytes(first_32_bytes_latin_1, 'little')
        int_value_big_latin_1 = int.from_bytes(first_32_bytes_latin_1, 'big')
        int_value_little_cp1252 = int.from_bytes(first_32_bytes_cp1252, 'little')
        int_value_big_cp1252 = int.from_bytes(first_32_bytes_cp1252, 'big')
        int_value_little_iso_8859_2 = int.from_bytes(first_32_bytes_iso_8859_2, 'little')
        int_value_big_iso_8859_2 = int.from_bytes(first_32_bytes_iso_8859_2, 'big')
        int_value_little_gbk = int.from_bytes(first_32_bytes_gbk, 'little')
        int_value_big_gbk = int.from_bytes(first_32_bytes_gbk, 'big')
        int_value_little_shift_jis = int.from_bytes(first_32_bytes_shift_jis, 'little')
        int_value_big_shift_jis = int.from_bytes(first_32_bytes_shift_jis, 'big')

        # Convert each integer into a private key
        private_key_little_utf8 = self.int_to_private_key(int_value_little_utf8)
        private_key_big_utf8 = self.int_to_private_key(int_value_big_utf8)
        private_key_little_ascii = self.int_to_private_key(int_value_little_ascii)
        private_key_big_ascii = self.int_to_private_key(int_value_big_ascii)
        private_key_little_utf16 = self.int_to_private_key(int_value_little_utf16)
        private_key_big_utf16 = self.int_to_private_key(int_value_big_utf16)
        private_key_little_utf32 = self.int_to_private_key(int_value_little_utf32)
        private_key_big_utf32 = self.int_to_private_key(int_value_big_utf32)
        private_key_little_latin_1 = self.int_to_private_key(int_value_little_latin_1)
        private_key_big_latin_1 = self.int_to_private_key(int_value_big_latin_1)
        private_key_little_cp1252 = self.int_to_private_key(int_value_little_cp1252)
        private_key_big_cp1252 = self.int_to_private_key(int_value_big_cp1252)
        private_key_little_iso_8859_2 = self.int_to_private_key(int_value_little_iso_8859_2)
        private_key_big_iso_8859_2 = self.int_to_private_key(int_value_big_iso_8859_2)
        private_key_little_gbk = self.int_to_private_key(int_value_little_gbk)
        private_key_big_gbk = self.int_to_private_key(int_value_big_gbk)
        private_key_little_shift_jis = self.int_to_private_key(int_value_little_shift_jis)
        private_key_big_shift_jis = self.int_to_private_key(int_value_big_shift_jis)

        # add additional ways to generate a private key from the string
        asciiPrivateKey = self.generate_private_key_from_string_ascii(string)
        md5PrivateKey = self.generate_private_key_from_string_md5(string)
        sha256PrivateKey = self.sha256WordToPrivateKey(string)

        returnArray = [private_key_little_utf8, private_key_big_utf8, private_key_little_ascii, private_key_big_ascii, private_key_little_utf16, private_key_big_utf16, private_key_little_utf32, private_key_big_utf32, private_key_little_latin_1, private_key_big_latin_1, private_key_little_cp1252, private_key_big_cp1252, private_key_little_iso_8859_2, private_key_big_iso_8859_2, private_key_little_gbk, private_key_big_gbk, private_key_little_shift_jis, private_key_big_shift_jis, sha256PrivateKey, md5PrivateKey, asciiPrivateKey]
        # remove duplicate from return array
        returnArrayUnique = list(dict.fromkeys(returnArray))

        # Return the private keys
        return returnArrayUnique

        # create a function to generate an address from a string
    def generate_private_key_from_string_md5(self, string):
        # use md5 to hash the string
        # print("String: ********** MD5 " + str(string))
        md5Hash = hashlib.md5(string.encode())
        md5HashInt = int(md5Hash.hexdigest(), 16)
        return self.int_to_private_key(md5HashInt)
    


    def generate_private_key_from_string_ascii(self, string):
       
    #    turn each character into a number
        numbers = ""
        for char in string:
            numbers = numbers + str(ord(char))
        
        if numbers == "":
            numbers = "0"

        integer = int(numbers)

        if integer > self.maxIntAllowed:
            # remove the last digets until  is less then maxNumber
            while integer > self.maxIntAllowed:
                integer = int(str(integer)[:-1])

        return self.int_to_private_key(integer)
    

    def sha256WordToPrivateKey(self, string):
        # use md5 to hash the string
        # print("String: ********** MD5 " + str(string))
        hexNumber = sha256(string.encode('utf-8')).hexdigest()
        number = int(hexNumber, 16)
        return self.int_to_private_key(number)