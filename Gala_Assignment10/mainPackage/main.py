# File Name : Gala_Assignment10
# Student Name: Jack Driehaus 
# email:  driehajl@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   04/10/2025
# Course #/Section:   Is4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Getting interesting info out of a public API

# Brief Description of what this module does. Instantiates the function from APIStuff to print the quote and character info
# Citations: 

# Anything else that's relevant:


#https://gameofthronesquotes.xyz/
#https://github.com/shevabam/game-of-thrones-quotes-api

if __name__ == "__main__":
    from APIStuff.API import character_quote

    quote, character = character_quote()
    print('"'+ quote +'"')
    print(character)
    

    

