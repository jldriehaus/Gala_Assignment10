# File Name : Gala_Assignment10
# Student Name: Jack Driehaus, Madison Geier
# email:  driehajl@mail.uc.edu, geierml@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   04/10/2025
# Course #/Section:   Is4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Getting interesting info out of a public API

# Brief Description of what this module does. Instantiates the function from APIStuff to print the quote and character info
# Citations: https://learnpython.com/blog/python-json-to-csv/ 

# Anything else that's relevant:


#https://gameofthronesquotes.xyz/
#https://github.com/shevabam/game-of-thrones-quotes-api

if __name__ == "__main__":
    from APIStuff.API import character_quote

import csv
from APIStuff.API import character_quote

def save_to_csv(quote, character):
    filename = "got_quotes.csv"  # Defining our filename

   
    character_name = character.get('name', 'Unknown')
    house_name = character.get('house', {}).get('name', 'None')

    
    try:
        with open(filename, mode='x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Quote', 'Character', 'House'])  # write headers
    except FileExistsError:
        pass  

    # Append new row of data
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([quote, character_name, house_name])

if __name__ == "__main__":
    quote, character = character_quote()
    print(f'"{quote}"')
    print(character)

    save_to_csv(quote, character)  


    quote, character = character_quote()
    print('"'+ quote +'"')
    print(character)
    

    

