VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'


import random

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        
    def addMoney(self, amt):
        self.prizeMoney+=amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self,prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)



# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def __init__(self, name):
        WOFPlayer.__init__(self,name)
     
    def getMove(self, category, obscuredPhrase, guessed):
        move = input("""
            {} has ${}
            
            Category: {}
            Phrase:   {}
            Guessed:  {}
            
            Guess a letter, phrase, or type 'exit' or 'pass':
            """.format(self.name, self.prizeMoney,category, obscuredPhrase, ', '.join(sorted(guessed))))
        
        return move


# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self,name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        randNumber = random.randint(1, 10)
        if randNumber > self.difficulty:
            return False
        else:
            return True

    def getPossibleLetters(self, guessed):

        if self.prizeMoney >= VOWEL_COST:
            possibleLetters = [l for l in LETTERS if l not in guessed]
        else:
            possibleLetters = [l for l in LETTERS if l not in guessed and l not in VOWELS]

        return possibleLetters

    def getMove(self, category, obscuredPhrase, guessed):
        
        if (self.prizeMoney < VOWEL_COST) and (self.getPossibleLetters(guessed) == [v for v in VOWELS]):
            return 'pass'
        else: 
            if self.smartCoinFlip() == True:
                return self.SORTED_FREQUENCIES[-1]
            else:
                return random.choice(self.SORTED_FREQUENCIES)


       

