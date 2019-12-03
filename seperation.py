# Compulsory Task 3

# Allows the user to input a paragraph or sentence
string = input ("Type your sentence or paragragh here:\n")
# Splits the sentence into a list of words
lstWords = string.split()
# Counts the length of the list (The number of words)
wordCount = len (lstWords)
# Declares starting position = 0
position = 0

# This loop will run for the amount of words and then print the word in the position declared
for i in range (0,wordCount):
    print (lstWords[position])
    position += 1 # This updates the position so that the next word is printed
    
 
