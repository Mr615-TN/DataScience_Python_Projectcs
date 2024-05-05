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