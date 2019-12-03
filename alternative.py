# Compulsory Task 1

# Here the string variable is declared aswell as the starting position
stringOld = ("Letter case is the distinction between the letters that are in larger upper case and smaller lower case in the written representation of certain languages.")
position = 0
# The string is then split into words ans split into letters or characters
stringWords = stringOld.split()
stringNoSpace = stringOld.replace(""," ")
stringLetters = stringNoSpace.split()

# This loop will run for the number of characters:
# If the characters position is divisable by 2 then it will be put in upper case
# If the characters position is not divisable by 2 then it will be put in lower case
# The variable poition is incremented by 1 for a new letter position
for i in range (0,len(stringLetters)):

    if position%2 == 0:
        stringLetters[position] = stringLetters[position].upper()
    if position%2 != 0:
       stringLetters[position] = stringLetters[position].lower()
    position += 1

# Here the wordNum is declared and the position is reset to 0
# The final string is declared as empty
wordNum = 0
position = 0
newString =""    

# This loop will run for the number of words in the string
# It counts the number of letters in the word in that position
# The wordNum is also incremented for the next loop 
for i in range (0, len(stringWords)):
    length = len(stringWords[wordNum])
    wordNum += 1
    # This loop will run for the length of the word and adds the consecutive letters until the word ends then adds a space.
    for i in range (0, length):
        newPos = stringLetters[position]
        newString = str(newString + newPos)
        position += 1
    newString = newString + " "

# The final new string is printed  
print (newString)
