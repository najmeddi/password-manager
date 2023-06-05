#!/usr/local/bin/python3


from Crypto.Cipher import AES

# =============================================
# ======= do not change these values ==========
# =============================================


CTR_NONCE = b'PzphkGKm'
KEY_LEN = 16
# =============================================
# ========= write your code below  ============
# =============================================
import math

MIN_KEY_SIZE = 4
'''(str) -> bytes
Encodes a string to bytes in utf-8
'''
def toBytes(s):
   return bytes(s, 'utf-8') 

'''(bytes) -> bool
Checkes if a key is of proper size
'''
def checkKeySize(k):
   if(len(k) == KEY_LEN):
      return True
   return False

def getKey():
   is_good_key = False
   key = b''
   
   while(not is_good_key):
      key_input = input("Enter the key: ")
      key = toBytes(key_input)
      if (checkKeySize(key)):
         is_good_key = True
      elif(len(key) >= 4 and len(key) <= KEY_LEN):
         key_padded = key_input * (math.ceil(KEY_LEN / len(key_input)))
         key = toBytes(key_padded[:16])
         if (checkKeySize(key)):
            is_good_key = True         
      else:
         print("Enter a key that is of proper length")
   
   return key

def encrypt(inputFileName, outputFileName='testoutput.txt'):
   ''' 
   Encrypts the image inputFile with the keyFile using the aes cipher (from PyCryptodome) 
   and writes the image outputFile
   The image outputFile must be a viewable image file.
   (string, string, string, string) -> None
   '''
   
   # Open the text document to encrypt
   inputFile = open(inputFileName, 'rb')
   
   inputText = inputFile.read()
   
   # Get the key for encrypting the text
   key = getKey()
   
   # Encrypt the plaintext with the given key
   ciphertext = b''
   cipher = AES.new(key, AES.MODE_CTR, nonce=CTR_NONCE)
   ciphertext = cipher.encrypt(inputText)
  
   inputFile.close()
   
   # Output the result in a new file
   outputFile = open(outputFileName, 'wb')
   outputFile.write(ciphertext)
   outputFile.close()
   
   return ciphertext 

def decrypt(inputFileName):
   ''' 
   Decrypts the image inputFile with the keyFile using the aes cipher (from PyCryptodome) 
   and writes the image outputFile
   The image outputFile must be a viewable image file.
   (string, string, string, string) -> None
   '''
   # Open the text document to encrypt
   inputFile = open(inputFileName, 'rb')
   
   inputText = inputFile.read()
   
   # Get the key for encrypting the text
   key = getKey()
   
   # Encrypt the plaintext with the given key
   plaintext = b''
   cipher = AES.new(key, AES.MODE_CTR, nonce=CTR_NONCE)
   plaintext = cipher.decrypt(inputText)
  
   inputFile.close()
   
   
   
   return plaintext

# =============================================
# ===== do not modify the code below ==========
# =============================================

if __name__ == "__main__":
   pass