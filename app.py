"""Form Pig Latin by adding 'ay' at the end of a word. Add 'way'if it starts with a vowel."""
#Import the required module(s)
import sys

#Declare the vowels
vowels = 'aeiou'

while True:
    #Ask user to input a word
    word = input("Type a word to see it's Pig Latin translation: ")

    #Check if first letter is a vowel then add 'way' at the end of the word.
    if word[0] in vowels:
        pig_latin = word+'way'
    #If first letter is not a vowel, move it at the end then add 'ay'
    else:
        pig_latin = word[1:] + word[0] +'ay'
    print()
    print("{}".format(pig_latin))

    #Ask the user to try again or quit.
    try_again = input("\n\nTry again?(Press Enter, else, n to stop)\n")
    if try_again.lower() =="n":
        sys.exit()