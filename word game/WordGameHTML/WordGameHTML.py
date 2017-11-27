import random 
import time
import pickle
from itertools import islice
from collections import Counter
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "lfvDLFKgDFKGdfgadfLKhndFjAgdaFAHdfgj:DFAjhhjhjhdfLJ"

longWords = []
lowercaseWords = []
messages = [] 
timeBegin = 0.0
timeOver = 0.0
timeTotal = 0

@app.route('/')
def get_and_display_form():
	rulesObeyed = True

	##Reading from text file and assigning to variable.
	with open("Words.txt", errors = 'ignore') as text_file:
		wordDoc = text_file.read()
		
	#spliting doc into individual words   
	words = wordDoc.split()

	#get rid of small, impossible words and convert to lower case
	for word in words:
		if(len(word)  >= 7):
			longWords.append(word.lower())

	return render_template('StartMenu.html')


@app.route('/Play')
def outputWord():
	gameOn = True

	#fetch random work form the word list
	randomWord = random.choice(longWords)

	return render_template('PlayGame.html', word=randomWord)

@app.route('/processform', methods=['POST'])
def processform():

	words = request.form['wordInput']
	#make words all lower case for checking
	words = words.split()

	return render_template('Results.html', words = words)


if __name__ == '__main__':
    app.run(debug=True)