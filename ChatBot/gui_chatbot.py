import nltk
from nltk.stream import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.model import load_model

model = load_model('chatbot_model.h5')

import json
import random

possibleIntents = json.loads(open('intents.json')).read()
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def clean_up(sentence):
    words_in_sentence = nltk.word_tokenize(sentence)
    words_in_sentence = [(lemmatizer.lemmatize(word.lower()) for word in words_in_sentence)]

    return words_in_sentence

def bag_o_words(sentence, words, show_details = True):
    words_in_sentence = clean_up(sentence)

    bag_words = [0]*len(words)
    for s in words_in_sentence:
        for i,word in enumerate(words):
            if word == s:
                bag_words[i] = 1
                if show_details:
                    print("Found in bag: %s" % word)

    return(np.array(bag_words))

def prediction(sentence):
    p = bag_o_words(sentence, words, show_details=False)
    reso = model.predict(np.array([p]))[0]

    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(reso) if r > ERROR_THRESHOLD]

    results.sort(key = lambda x: x[1], reverse = True)

    return_list = []
    for resulto in results:
        return_list.append({"intent": classes[resulto[0]], "probability": str(resulto[1])})
    return return_list

def returnResponse(ints, intents_json):
    tag = ints[0]['intent']

    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result


import tkinter
from tkinter import *

def send():
    messag = EntryBox.get("1.0","end-1c").strip()
    EntryBox.delete("0.0", END)

    if messag != '':
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END, "You: " + messag + '\n\n')
        ChatBox.config(foreground = "#446665", font=("Verdana", 12))

        ints = prediction(messag)

        resol = returnResponse(ints, possibleIntents)

        ChatBox.insert(END, "Bot: " + resol + '\n\n')
        ChatBox.config(state=DISABLED)

        ChatBox.yview(END)

root = Tk()

root.title("Chatbot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

ChatBox = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatBox.config(state=DISABLED)

scrollbar = Scrollbar(root, command=ChatBox.yview, cursor="heart")

ChatBox['yscrollcommand'] = scrollbar.set

SendButton = Button(root, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#f9a602", activebackground="#3c9d9b",fg='#000000',
                    command= send )
EntryBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial")

scrollbar.place(x=376,y=6, height=386)
ChatBox.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

root.mainloop()