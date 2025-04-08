# File Name : Gala_Assignment10
# Student Name: Jack Driehaus, Madison Geier
# email:  driehajl@mail.uc.edu, geierml@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   04/10/2025
# Course #/Section:   Is4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Getting interesting info out of a public API

# Brief Description of what this module does. Uses the API URL to receive info from the server about the GOT quote 
# Citations: 

# Anything else that's relevant:

import json
import requests


def character_quote():
    response = requests.get('https://api.gameofthronesquotes.xyz/v1/random?characters=jon')
    json_string = response.content

    parsed_json = json.loads(json_string) # Now we have a python dictionary

    sentence = parsed_json['sentence']    # Gets the character's quote
    character = parsed_json['character']   # Gets the information about the character (name, house, etc.)

    return sentence, character