import numpy as np 
from keras.models import Sequential 
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD 

import random

import nltk
from nltk.stream import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import json
import pickle 

files = open('intents.json').read()
intents = json.loads(files)


#Preprocess Data
words = []
classes = []
documents = []

ignoreLetters = ['!', '?', ',', '.']

for possible_intent in intents['intents']:
    for possible_patterns in intents['patters']:
        word = nltk.word_tokenize(possible_patterns)
        documents.append((word, possible_intent['tag']))
        if possible_intent['tag'] not in classes:
            classes.append(possible_intent['tag'])
print(documents)

#lemmatize
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignoreLetters]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique lemmatized words", words)

pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

#train data
training = []
emptyArray = [0] * len(classes)

for doc in documents:
    bag_of_words = []
    wordPatterns = doc[0]

    wordPatterns = [lemmatizer.lemmatize(word.lower()) for word in wordPatterns]
    for word in words:
        bag_of_words.append(1) if word in wordPatterns else bag_of_words.append(0)
    
    row_output = list(emptyArray)
    row_output[classes.index(doc[1])] = 1

    training.append([bag_of_words, row_output])

random.shuffle(training)
training = np.array(training)

x = list(training[:,0])
y = list(training[:,1])

print("Training data created")