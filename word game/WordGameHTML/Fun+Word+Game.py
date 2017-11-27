import random 
import time
import pickle
from itertools import islice
from collections import Counter
from flask import Flask, render_template, request

app = Flask(__name__)

longWords = []

##Reading from text file and assigning to variable.
with open("Words.txt", errors = 'ignore') as text_file:
    wordDoc = text_file.read()
    
#spliting doc into individual words   
words = wordDoc.split()

#get rid of small, impossible words and convert to lower case
for word in words:
    if(len(word)  >= 7):
        longWords.append(word.lower())

gameOn = True

#game loop
while(gameOn == True):
    timeBegin = 0.0
    timeOver = 0.0
    timeTotal = 0
    
    print("Current LeaderBoard: \n ")
    
    
    #show player the rules
    print('''Rules:

    1. Each word must be made up from letters contained within the source word 
    2. The words all have 3 or more letters. 
    3. There are no duplicate words 
    4. None of the 7 submitted words is the source word
    
    ''')
    
    #on your marks
    userVar = input("Press y when ready \n")

    while(userVar != "y" and userVar != "Y"):
        userVar = input("Press Y when ready please \n")
    
    #fetch random work form the word list
    randomWord = random.choice(longWords)
    
    print('''make 7 words out of the following word
          follow the rules above 
          seperate the words with a space
          ''')
    
    timeBegin = time.time()
    
    userVar = input("Your word is " + randomWord + "\n")
    
    timeOver = time.time()
    
    rulesObeyed = True
    
    #split the user input into individual words
    
    userWords = userVar.split(" ")
    
    lowercaseWords = []
    
    #make words all lower case for checking
    for word in userWords:
        lowercaseWords.append(word.lower())
    
    print(lowercaseWords)
    
    ### rules followed checking
    
    #check if the word is the same as the given word
    for word in lowercaseWords:
        if(word == randomWord):
            print("You cannot use the given word!!")
            rulesObeyed = False
    
    #check if each word is a word
    for word in lowercaseWords:
        if(word not in words):
            print(word + " is not a word!!")
            rulesObeyed = False
    
    #check for duplicates
    if(len(lowercaseWords) != len(set(lowercaseWords))):
       print("Duplicates found!!")
       rulesObeyed = False
    
    #not too many words
    if(len(lowercaseWords) < 7):
        print("Too few words \n")
        rulesObeyed = False
    
    #not too few words
    if(len(lowercaseWords) > 7):
        print("Too many words!!")
        rulesObeyed = False
        
    #check if word is too small
    for word in lowercaseWords:
        if(len(word) < 3):
            print(word + " is too small!!")
            rulesObeyed = False
    
    #check letters arent repeated
    for word in lowercaseWords:
        countBigWord = Counter(randomWord)
        countUser = Counter(word)
        countBigWord.subtract(countUser)

        for letter in countBigWord:
            if(countBigWord[letter] < 0):
                print("letters repeated in " + word + "!!")
                rulesObeyed = False
     
    if(rulesObeyed == True):
        timeTotal = timeOver - timeBegin  
        print("Time taken: " + "{0:.3f}".format(timeTotal))
        
        username = input("Please enter your username: ")
        
        leaderboard = {}
        
        ##Loads back from pickle
        leaderboard = pickle.load( open( "leaderboard.p", "rb" ) )
        
        ##Adds a new key & value to the dictionary ( key -> score: name <- Value)
        leaderboard["{0:.3f}".format(timeTotal)] = username
    
        ##Writes to pickle file (overrites while at it)
        pickle.dump(leaderboard, open( "leaderboard.p", "wb" ) )

        ##Loads back from pickle
        leaderboard = pickle.load( open( "leaderboard.p", "rb" ) )
        
        ##Sorts by key value
        sortedScores = {(leaderboard[k], k) for k in sorted(leaderboard, key=leaderboard.get, reverse=False)}
        
        ##Gives X first in list. (in this example, X = 5)
        topTen = list(islice(sortedScores, 10))
        
        print(leaderboard)
        
        print("Leaderboard Top 10 \n \n")
        
        ##Prints the key and value (0 = key, 1 = value)
        for row in topTen:
            print(row[1], row[0])
        
        
    #quit game option to break out of loop
    userVar = input("would you like to quit? Y/N   \n")
    while(userVar != "y" and userVar != "Y" and userVar != "n" and userVar != "N"):
        userVar = input("Y or N please \n")
        
    if(userVar == "y" or userVar == "Y"):
        gameOn = False
    

