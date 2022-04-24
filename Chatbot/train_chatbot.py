from keras.layers import Dense, Activation, Dropout
import random
from keras.optimizers import sgd_experimental
from keras.models import Sequential
import numpy as np
import json
import nltk
import pickle
from nltk import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

words = []
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open('D:\hello\Chatbot\intents.json').read()
intents = json.loads(data_file)

# pre process data
for intent in intents['intents']:
    for pattern in intent['patterns']:

        # tokenize each word
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # add documents in the corpus
        documents.append((w, intent['tag']))

        # add to our classes
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lemmatize, lower each word and remove duplicates
words = [lemmatizer.lemmatize(w.lower())
         for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# sort classes
classes = sorted(list(set(classes)))

# documents = combination between patterns and intents
print(len(documents), "documents")

#classes = intents
print(len(classes), "classes", classes)

# words = all words, vocabulary
print(len(words), "unique lemmatized words", words)

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# create training and testing
# Create training data
training = []

# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []

    # list of tokenized words for the pattern
    pattern_word = doc[0]

    # lemmatize each word - create base word, in attempt to represent related words
    pattern_word = [lemmatizer.lemmatize(words.lower()) for word in pattern]

    # create our bag of words array with 1, if word match found in current pattern
    for w in words:
        bag.append(1) if w in pattern_word else bag.append(0)

    # output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)
# create train and test list. X - patterns , Y - intents
train_x = list(training[:, 0])
train_y = list(training[:, 1])
print("Training data created")


# Build Model
# create model - 3 layers, first layer 128 neurons, second layer 64 neurons
