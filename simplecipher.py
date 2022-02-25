# This will demo simple cipher algorithms
# Author: Alexander Sutter
# Date: 2/10/22
# Latest Revision: 2/11/2022

import string
from time import time

# put cipher algorithms 
def ceasarCipher(mode, text):
  result = ''

  shift = -3
  
  if mode == 'enc':
    for letter in text:
      num = ord(letter)
      num += shift
      result += chr(num)
  elif mode == 'dec':
    for letter in text:
      num = ord(letter)
      num -= shift
      result += chr(num)
  else:
    return 'invalid mode'
  
  return result

def atbashCipher(text):
  result = ""
  
  alphaString = string.ascii_letters
  alpha = []
  for letter in alphaString:
    alpha.append(letter)
  alphaReverse = alpha
  alphaReverse.reverse()

  # text = text.upper()
  
  # encode & decode
  for i in range(len(text)):
    if text[i] != " ":
      location = alphaString.index(text[i])
      result += alphaReverse[location]
    else:
      result += text[i]
  
  return result

def railFenceCipher(mode, text):
  result = ''
  
  # check length (only works for even number of characters)
  if len(text) % 2 != 0:
    text += " "
    if mode == 'dec':
      print("decryption may have fault!!")
  
  # encode
  if mode == 'enc':
    for i in range(0,len(text),2):
      result += text[i]
    # print(result)

    for i in range(1,len(text),2):
      result += text[i]
    # print(result)

  # decode
  elif mode == 'dec':
    halfPoint = int(len(text)/2)
    front = text[:halfPoint] #up to half point
    back = text[halfPoint:]
    
    for i in range(halfPoint):
      result += front[i]
      result += back[i]
    
    #not working implementation of algorithm
    # dec_txt = ''

    # for i in range(0,len(text),1):
    #   try:
    #     dec_txt += text[i]
    #     dec_txt += text[(len(text)//2)+i]
    #   except:
    #     break
    # # print(dec_txt)
    # result = dec_txt[:len(dec_txt)-1]
    # results = makeString(dec_txt)
    
    # print(len(text))
    # print(len(result))

  else:
    return 'invalid mode'

  return result

def createVigenereCipherTable(alpha):
  table = []
  
  for i in range(len(alpha)):
    row = []
    newalpha = alpha[i:] + alpha[:i]
    
    for letter in newalpha:
      row.append(letter)
    table.append(row)
  
  return table

def vigenereCipher(mode, key, text):
  result = ''

  # table = []
  alphaUpper = string.ascii_uppercase
  alphaLower = string.ascii_lowercase

  # create cipher chart
  tableUpper = createVigenereCipherTable(alphaUpper)
  tableLower = createVigenereCipherTable(alphaLower)
  
  # print(newalpha)
  # print(tableUpper)
  
  # text = text.upper()
  key = key.upper()

  # encode
  if mode == 'enc':
    offset = 0
    timesThrough = 1
    
    # create cipher via encryption
    for i in range(len(text)):
      # creation of col
      col = alphaUpper.index(text[i].upper()) #location across horizontal of text letter
      # print(y)
      
      # creation of row
      if i >= len(key) * timesThrough:
        offset = timesThrough * len(key)
        timesThrough += 1
      row = alphaUpper.index(key[i-offset]) #location across vertical of key letter
      # print(x)
      
      # print(row, col)
      # find cipher letter in correct case (uppercase or lowercase)
      if text[i] in alphaUpper:
        result += tableUpper[row][col]
      elif text[i] in alphaLower:
        result += tableLower[row][col]
  
  # decode
  elif mode == 'dec':
    # print(text)
    # text = text.upper()
    
    offset = 0
    timesThrough = 1
    
    for i in range(len(text)):
      # creation of row 
      if i >= len(key) * timesThrough:
        offset = timesThrough * len(key)
        timesThrough += 1
      row = alphaUpper.index(key[i-offset]) #location across vertical of key letter
      
      # creation of col while checking case(uppercase or lowercase)
      if text[i] in alphaUpper:
        for col in range(len(alphaUpper)):
          if tableUpper[row][col] == text[i]:
            result += alphaUpper[col]
            break
      elif text[i] in alphaLower:
        for col in range(len(alphaLower)):
          if tableLower[row][col] == text[i]:
            result += alphaLower[col]
            break
      # print(row, col)
      
  else:
    return 'invalid mode'
  
  return result

#make better vigenere cipher include uppercase lowercase and digits and spaces
def upgradedVigenereCipher(mode, key, text):
  result = ''
  
  alpha = string.ascii_letters
  digits = string.digits
  punctuation = string.punctuation
  
  characters = alpha + " " + digits + punctuation
  
  # create cipher chart
  table = createVigenereCipherTable(characters)
  # print(table)
  
  # print(newalpha)
  # print(characters)
  # print(len(key), len(text))
  
  # encode
  if mode == 'enc':
    offset = 0
    timesThrough = 1
    
    # create cipher via encryption
    for i in range(len(text)):
      # creation of col
      col = characters.index(text[i]) #location across horizontal of text letter
      # print(y)
      
      # creation of row
      if i >= len(key) * timesThrough:
        offset = timesThrough * len(key)
        timesThrough += 1
      row = characters.index(key[i-offset]) #location across vertical of key letter
      # print(row)
      # print(x)
      
      # print(row, col)
      # find cipher letter in correct case (uppercase or lowercase)
      result += table[row][col]
  
  # decode
  elif mode == 'dec':
    # print(text)
    # text = text.upper()
    
    offset = 0
    timesThrough = 1
    
    for i in range(len(text)):
      # creation of row 
      if i >= len(key) * timesThrough:
        offset = timesThrough * len(key)
        timesThrough += 1
      row = characters.index(key[i-offset]) #location across vertical of key letter
      
      # creation of col while checking case(uppercase or lowercase)
      for col in range(len(characters)):
        if table[row][col] == text[i]:
          result += characters[col]
          break
      # print(row, col)
      
  else:
    return 'invalid mode'
  
  return result

def main():
  # Ceasar Cipher
  text = 'Welcome to jamaica everything is irie and have a nice day'
  encryptedText = ceasarCipher('enc', text)
  decryptedText = ceasarCipher('dec', encryptedText)

  print('\n-  -  -  -  caesar cipher  -  -  -  -')
  print(text)
  print(encryptedText)
  print(decryptedText + "\n")

  # Atbash Cipher
  text = 'Welcome to jamaica everything is irie and have a nice day'
  encryptedText = atbashCipher(text)
  decryptedText = atbashCipher(encryptedText)

  print('\n-  -  -  -  atbash cipher  -  -  -  -')
  print(text)
  print(encryptedText)
  print(decryptedText + "\n")

  # Rail Fence Cipher
  text = 'Welcome to jamaica everything is irie and have a nice day'
  encryptedText = railFenceCipher('enc', text)
  decryptedText = railFenceCipher('dec', encryptedText)

  print('\n-  -  -  -  rail fence cipher  -  -  -  -')
  print(text)
  print(encryptedText)
  print(decryptedText + "\n")

  # Vigenere Cipher
  text = 'Cat'
  key = 'horse'
  encryptedText = vigenereCipher('enc', key, text)
  decryptedText = vigenereCipher('dec', key, encryptedText)

  print('\n-  -  -  -  vigenere cipher  -  -  -  -')
  print(text)
  print(encryptedText)
  print(decryptedText + "\n")
  
  # Upgraded Vigenere Cipher
  # text = 'Cats :) ! Hi Professor, I made this for fun thought the plain cipher was a little lacking'
  # key = 'horses and ponies with spears on their heads and rainbows lots of rainbows '
  
  text = "My password is password"
  key = "horse"
  encryptedText = upgradedVigenereCipher('enc', key, text)
  decryptedText = upgradedVigenereCipher('dec', key, encryptedText)

  print('\n-  -  -  -  upgraded vigenere cipher  -  -  -  -')
  print(text)
  print(encryptedText)
  print(decryptedText + "\n")

main()