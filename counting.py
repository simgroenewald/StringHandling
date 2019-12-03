# Compulsory Task 2

# String can be entered here
string = input("Please type your sentence or paragraph here:\n")

# This put the string in lower case for the counting process
string = string.lower()

# This takes away any spaces in the string to count the amount of characters which is then calculated
stringNoSpace = string.replace (" ","")
charTotal = len(stringNoSpace)

# This puts spaces between all the characters so that a list can be formed where each character is in a different position
stringAllSpace = stringNoSpace.replace (""," ")
charLst = stringAllSpace.split()

# This declares the starting position and an empty string which will be the final output
position = 0
letterCount = ""

# The loop runs for the length of all the characters in the string
for i in range (0,charTotal):
    # The position value that will be compared to the starting positions value is declared and needs to be updated every time the loop runs so that it starts at the beginning of the string
    posCompare = 0
    # The counter is reset to 0 every time
    count = 0

    # This loop will also run for the length of the string
    for i in range (0,charTotal):

        # Here two letters are declared in the variables letter and letterCompare and if they are equal in value then the counter is increased by 1. The poition that is compared gets updated and the loop runs again
        # If the letter variable is found in the already existing output string then the loop breaks so that letters are not duplicated in the output string
        letterEqual = False
        letter = charLst[position]
        letterCompare = charLst [posCompare]
        letterUsed = letterCount.find(letter)
        if letterUsed > 0:
            break 
        elif letter == letterCompare:
            letterEqual = True
            if letterEqual == True:
                count += 1
        posCompare += 1

    # Here the position gets updated to have a new starting position and letter variable for the next run of the loop
    position += 1
    # The the count for any letter is 0 due to th previous loop breaking then the output string is not updated. It will only update if there counting took place
    if count > 0:
        letterCount = letterCount + "'" + letter + "'" + ":" + str(count)+ ","
    
# The final output string is printed
letterCountDisplay = letterCount.strip(",")
letterCountDisplay = "{" + letterCountDisplay + "}"
print (letterCountDisplay)
    




    
    
