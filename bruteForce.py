# This will demo a brute force attack against the Caesar Cipher & the Vigenère Cipher
# Author: Alexander Sutter
# Date: 2/23/22
# Latest Revision: 2/23/2022

import string

def ceasarBrute(encText):
    results = []
    
    encText = encText.upper()
    alpha = string.ascii_uppercase
    
    for shift in range(26):
        possText = ""
        for letter in encText:
            if letter in alpha:
                index = alpha.index(letter)
                index += shift
                if index >= 26:
                    index -= 26
                possText += alpha[index]
            else:
                possText += letter
        results.append(possText)
    
    return results

def createVigenereCipherTable(alpha):
    table = []
  
    for i in range(len(alpha)):
        row = []
        newalpha = alpha[i:] + alpha[:i]
        
        for letter in newalpha:
            row.append(letter)
        table.append(row)
    
    return table

def generateKey(lastKey):
    print("Last Key: " + lastKey)
    
    alpha = string.ascii_uppercase
    newKey = ""
    
    if lastKey == "":
        newKey = 'A'
    
    elif lastKey == 'Z' * len(lastKey):
        print("************************************")
        newKey = 'A' * (len(lastKey) +1)
    
    else: 
        for letter in lastKey:
            # fix by rotate only 1
            index = alpha.index(letter)
            index += 1
            if index >= 26:
                index -= 26
            newKey += alpha[index]
    
    print("New Key: " + newKey)
    return newKey

def vigenereBrute(encText):
    results = []

    # table = []
    alphaUpper = string.ascii_uppercase
    alphaLower = string.ascii_lowercase

    # create cipher chart
    tableUpper = createVigenereCipherTable(alphaUpper)
    tableLower = createVigenereCipherTable(alphaLower)
    
    tries = 70
    key = ""
    
    index = 0
    while index < tries :
        #generate key to try
        key = generateKey(key)
        
        results.append(key)
        index += 1
        
        # possText = ""
        # offset = 0
        # timesThrough = 1
        
        # for i in range(len(encText)):
        #     if encText[i] in alphaUpper:
        #         table = tableUpper
        #     elif encText[i] in alphaLower:
        #         table = tableLower
            
        #     # creation of row 
        #     if i >= len(key) * timesThrough:
        #         offset = timesThrough * len(key)
        #         timesThrough += 1
        #     row = alphaUpper.index(key[i-offset]) #location across vertical of key letter
            
        #     # creation of col
        #     for col in range(len(alphaUpper)):
        #         if table[row][col] == encText[i]:
        #             possText += alphaUpper[col]
        #             break
            
        # results.append("key: " + key + " = " + possText)
        # index += 1
    
    return results

def openFile(fileName="fileReadingWriting_Base_Default.txt"):
    try:
        return open(fileName, "a")
    except:
        print("error opening file")

def writeFile(fileName, data, completeLine = True):
    file = openFile(fileName)
    if completeLine:
        file.write(data + "\n")
    else: 
        file.write(data)
    file.close()

def printList(list):
    itemNum = 0
    data = "" # for text file printing
    for item in list:
        # print(str(itemNum) + ": " + item) #for command line printing
        
        dataItem = str(itemNum) + ": " + item
        data += dataItem + "\n" # for text file printing
        
        itemNum += 1
    
    writeFile("hack.txt", data)

def main():    
    ciphertext = "GUVF VF ZL FRPERG ZRFFNTR."
    
    # Brute Force Ceasar Cipher
    # cearsarDecryptedList = ceasarBrute(ciphertext)

    # print('\n-  -  -  -  caesar cipher brute force  -  -  -  -')
    # print(ciphertext)
    # printList(cearsarDecryptedList)
    
    ciphertext = "Jok"
    
    # Brute Force Vigenere Cipher
    vigenereDecryptedList = vigenereBrute(ciphertext)
    
    print('\n-  -  -  -  vigenere cipher brute force  -  -  -  -')
    print(ciphertext)
    print("")
    printList(vigenereDecryptedList)
    
 
main()