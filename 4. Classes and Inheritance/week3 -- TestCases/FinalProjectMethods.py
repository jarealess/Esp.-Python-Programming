import json
import random
import time

###### getNumberBetween: Que solicita al usuario un número entre min, max, con el mensaje prompt

def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))

# getNumberBetween('Inserte un entero entre el rango especificado', 1, 10)

####--------------------------------------------------------------------------------------------------------------------
#### spinWheel que simula girar la rueda y devuelve un diccionario con un premio aleatorio
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)



###-----------------------------------------------------------------------------------------------------------------------
# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")
def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())



### ------------------------------------------------------------------------------------------------------------------------
# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
LETTERS = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

adivinado = obscurePhrase('THE GREAT WALL OF CHINA', ['R', 'Q', 'M', 'D', 'E', 'I', 'H', 'G', 'O', 'L', 'A', 'U', 'T', 'P', 'F'])
print(adivinado)


#### --------------------------------------------------------------------------------------------------------------
# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
    Category: {}
    Phrase:   {}
    Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

