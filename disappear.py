# Compulsory Task 4

# Allows the user to enter a paragraph or sentence and sets the remove letter value to false
string = input("Type you sentence or paragraph here:\n")
removeLetter = False

#This loop will run until it breaks
# It allows the user to decide if they would like to remove a letter. If yes then removeLetter become true and the inner loop runs. If no then the removeLetter becomes false and the loop breaks.
while 1:
    
    reqRemoveLetter = input("Would you like to remove a letter? (Yes or No): ")
    reqRemoveLetter = reqRemoveLetter.lower() # Ensures that the reponse is not case sensetive
    if reqRemoveLetter == "yes":
            removeLetter = True
    if removeLetter == False:
        break
    
    # This loop will run if the user wants to remove a letter
    # The user can choose which letter they would like to remove
    while removeLetter == True:
        dltChar = input ("Which letter do you want to remove: ")
        # This loop will run for the length of the string
        # It replaces the requested letter to be removed with nothing and updates the string
        for i in range (0, len(string)):
            string = string.replace(dltChar,"")
        print(string)
        removeLetter = False # The removeLetter variable then becomes f
        alse before the main loop to run again

print ("Your final sentence/paragraph is: " + string)

    
    
