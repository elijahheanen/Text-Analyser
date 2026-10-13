import string

with open("files/file.txt") as file: # Open file, put words into list and normalise ccapitalisation and remove punctuation
    global words
    words = file.read().split()

    for word in range(len(words)):
        words[word] = words[word].lower() # Make all lowercase

        words[word] = words[word].translate(str.maketrans('', '', string.punctuation)) # Remove punctuati punctuationn


def getFreqDict():
    #wordsAndFreq = {"word1": freq1, "word2", freq2}
    wordsAndFreq = {}
 
    for word in range(len(words)): # For each word in file
        currentWord = words[word]
        if not currentWord in wordsAndFreq: # If word not already found, add it to dictionary
            wordsAndFreq[currentWord] = 1
        else: # If word is already in dictionary, add one to its frequency
            wordsAndFreq[currentWord] = wordsAndFreq[currentWord]+1 

    return wordsAndFreq

print(getFreqDict())
